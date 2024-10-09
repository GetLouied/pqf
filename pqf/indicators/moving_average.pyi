from typing import overload

import polars as pl

@overload
def simple_moving_average(prices: pl.Series, window_size: int) -> pl.Series: ...
@overload
def simple_moving_average(prices: pl.Expr, window_size: int) -> pl.Expr: ...
@overload
def exponential_moving_average(prices: pl.Series, window_size: int) -> pl.Series: ...
@overload
def exponential_moving_average(prices: pl.Expr, window_size: int) -> pl.Expr: ...
