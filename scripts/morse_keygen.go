//go:generate go build -o ./morse_keygen $GOFILE

package main

import (
	"bufio"
	"encoding/base64"
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"text/tabwriter"

	"github.com/cometbft/cometbft/libs/rand"
	"github.com/spf13/cobra"

	"github.com/pokt-network/poktroll/pkg/polylog/polyzero"
	"github.com/pokt-network/poktroll/testutil/testmigration"
)

var (
	flagNumAccounts         = "num-accounts"
	flagShortNumAccounts    = "n"
	flagDistributionFn      = "dist-fn"
	flagShortDistributionFn = "d"
	flagDeterministic       = "deterministic"

	logger = polyzero.NewLogger(polyzero.WithLevel(polyzero.InfoLevel))

	numAccounts        int
	distributionFnName string
	deterministic      bool

	cmdGen = &cobra.Command{
		Use: "gen",
		// TODO_IN_THIS_COMMIT: ...
		//Short:                      "",
		//Long:                       "",
		//Example:                    "",
		Args: cobra.ExactArgs(0),
		RunE: runGen,
	}
)

const (
	roundRobinDistributionName     = "round-robin"
	allUnstakedDistributionName    = "unstaked"
	allApplicationDistributionName = "application"
	allSupplierDistributionName    = "supplier"
)

func init() {
	// TODO_IN_THIS_COMMIT: extract the following flags:
	// - distribution
	// - number of accounts
	// - output paths
	cmdGen.Flags().IntVarP(&numAccounts, flagNumAccounts, flagShortNumAccounts, 10, "The number of accounts to generate")
	cmdGen.Flags().StringVarP(&distributionFnName, flagDistributionFn, flagShortDistributionFn, roundRobinDistributionName, "The distribution function to use")
	cmdGen.Flags().BoolVar(&deterministic, flagDeterministic, false, "Whether to generate deterministic (index based; as opposed to random) accounts")
}

func main() {
	if err := cmdGen.Execute(); err != nil {
		logger.Error().Err(err).Msg("exiting due to error")
		os.Exit(1)
	}
}

func runGen(_ *cobra.Command, _ []string) error {
	distributionFn, err := getDistributionFn(distributionFnName)
	if err != nil {
		return err
	}

	morseStateExportJSONBz, morseAccountStateJSONBz, err := testmigration.NewMorseStateExportAndAccountStateBytes(numAccounts, distributionFn)
	if err != nil {
		return err
	}

	// TODO_IMPROVE: Add a flag to configure the directory path.
	keysDirPath := filepath.Join(".", "morse_keys")
	if err = ensureOutputDir(keysDirPath); err != nil {
		return err
	}

	if err := writePrivateKeys(keysDirPath); err != nil {
		return err
	}

	morseStateExportJSONPath := filepath.Join(keysDirPath, "morse_state_export.json")
	if err = os.WriteFile(morseStateExportJSONPath, morseStateExportJSONBz, 0644); err != nil {
		return err
	}

	morseAccountStateJSONPath := filepath.Join(keysDirPath, "morse_account_state.json")
	return os.WriteFile(morseAccountStateJSONPath, morseAccountStateJSONBz, 0644)
}

// TODO_IN_THIS_COMMIT: godoc and move...
func getDistributionFn(distributionFnName string) (distributionFn testmigration.MorseAccountActorTypeDistributionFn, err error) {
	switch distributionFnName {
	case roundRobinDistributionName:
		distributionFn = testmigration.RoundRobinAllMorseAccountActorTypes
	case allUnstakedDistributionName:
		distributionFn = testmigration.AllUnstakedMorseAccountActorType
	case allApplicationDistributionName:
		distributionFn = testmigration.AllApplicationMorseAccountActorType
	case allSupplierDistributionName:
		distributionFn = testmigration.AllSupplierMorseAccountActorType
	default:
		return nil, fmt.Errorf("unknown distribution function %q", distributionFnName)
	}

	return distributionFn, nil
}

// TODO_IN_THIS_COMMIT: godoc & move...
func ensureOutputDir(keysDirPath string) error {
	// Create the keys directory if it doesn't exist.
	keysDirExists, err := pathExists(keysDirPath)
	if err != nil {
		return err
	}

	// Check if the keys directory exists and prompt for
	// confirmation to overwrite it (delete and recreate).
	// TODO_IMPROVE: Add a flag to skip readline confirmation.
	if keysDirExists {
		shouldOverwrite, err := promptForOverwrite(keysDirPath)
		if err != nil {
			return err
		}
		if !shouldOverwrite {
			return nil
		}
		if err = os.RemoveAll(keysDirPath); err != nil {
			return err
		}
	}

	if err = os.MkdirAll(keysDirPath, 0755); err != nil {
		return err
	}
	return nil
}

// TODO_IN_THIS_COMMIT: godoc...
func writePrivateKeys(keysDirPath string) (err error) {
	// Construct a tab writer to write the all_keys_summary.txt file.
	// TODO_IMPROVE: Add a flag to configure the output file path.
	allKeysSummaryFilePath := filepath.Join(keysDirPath, "all_keys_summary.txt")

	allKeysSummaryFile, err := os.Create(allKeysSummaryFilePath)
	if err != nil {
		return err
	}

	writer := tabwriter.NewWriter(allKeysSummaryFile, 0, 0, 1, ' ', 0)
	defer func() {
		if err != nil {
			return
		}
		err = writer.Flush()
	}()

	// Write the header row.
	header := []string{"index", "seed", "address", "privKey (base64)"}
	if _, err := writer.Write([]byte(fmt.Sprintf("%s\n", strings.Join(header, "\t")))); err != nil {
		return err
	}

	for i := 0; i < numAccounts; i++ {
		var seed uint64
		switch deterministic {
		case true:
			seed = uint64(i)
		case false:
			seed = rand.Uint64()
		}

		// Generate, serialize, encrypt, and write the private key.
		privateKey := testmigration.GenMorsePrivateKey(seed)
		address := privateKey.PubKey().Address().String()
		pkBase64 := base64.StdEncoding.EncodeToString(privateKey)

		keyPath := filepath.Join(keysDirPath, fmt.Sprintf("%d_%s.key", i, address))
		keyArmoredJSON, err := testmigration.EncryptArmorPrivKey(privateKey, "", "")
		if err != nil {
			return err
		}

		if err = os.WriteFile(keyPath, []byte(keyArmoredJSON), 0644); err != nil {
			return err
		}

		// Write the key row to the all_keys_summary.txt file.
		if _, err = writer.Write([]byte(fmt.Sprintf("%d\t", i))); err != nil {
			return err
		}
		if _, err = writer.Write([]byte(fmt.Sprintf("%d\t", seed))); err != nil {
			return err
		}
		if _, err = writer.Write([]byte(fmt.Sprintf("%s\t", address))); err != nil {
			return err
		}
		if _, err = writer.Write([]byte(fmt.Sprintf("%s\n", pkBase64))); err != nil {
			return err
		}
	}

	return nil
}

// pathExists returns true if the given path exists, false otherwise.
func pathExists(path string) (bool, error) {
	if _, err := os.Stat(path); err != nil {
		if errors.Is(err, os.ErrNotExist) {
			return false, nil
		}
		return false, err
	}
	return true, nil
}

// promptForOverwrite prompts the user to confirm overwriting the given file.
func promptForOverwrite(filePath string) (shouldOverwrite bool, err error) {
	fmt.Printf("Morse keys directory %s already exists. Overwrite (this will delete all contents)? [y/N]: ", filePath)
	stdinReader := bufio.NewReader(os.Stdin)

	// This call to ReadLine() will block until the user sends a new line to stdin.
	inputLine, _, readErr := stdinReader.ReadLine()
	if readErr != nil {
		return false, readErr
	}

	switch string(inputLine) {
	case "y", "Y", "yes", "Yes", "YES":
		return true, nil
	default:
		return false, nil
	}
}
