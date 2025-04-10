from pocket_clients import ffi

DEFAULT_GAS_LIMIT = 200000
DEFAULT_GAS_ADJUSTMENT = 1.5


class GasSettings:
    def __init__(self,
                 gas_limit: int | None = None,
                 gas_prices: list[float] | None = None,
                 gas_adjustment: float | None = None,
                 fees: list[float] | None = None,
                 simulate: bool = False):
        self.gas_limit = gas_limit
        self.simulate = simulate
        self.gas_prices = gas_prices
        self.gas_adjustment = gas_adjustment
        self.fees = fees

        self._c_objects = []

    def to_c_struct(self) -> ffi.CData:
        c_gas_settings = ffi.new("gas_settings *")
        self._c_objects.append(c_gas_settings)
        c_gas_settings.simulate = self.simulate

        if self.gas_limit is not None:
            c_gas_settings.gas_limit = self.gas_limit

        if self.gas_adjustment is not None:
            c_gas_settings.gas_adjustment = self.gas_adjustment

        if self.gas_prices is not None:
            c_gas_settings.gas_prices = ffi.new(f"double", self.gas_prices)
            c_gas_settings.num_gas_prices = len(self.gas_prices)

        if self.fees is not None:
            c_gas_settings.fees = ffi.new(f"double", self.fees)
            self._c_objects.append(c_gas_settings.fees)

        return c_gas_settings


DefaultGasSettings = GasSettings(gas_limit=DEFAULT_GAS_LIMIT,
                                 simulate=True,
                                 gas_adjustment=DEFAULT_GAS_ADJUSTMENT,
                                 gas_prices=None,
                                 fees=None)
