 # Candlestick charting script, written in python using pandas and tkinter.


## It draws japanese candlestick charts from financial data.

### To achieve clarity it has bigger than usual level  of customisation.

### Optimised for small screen ⠀or ⠀huge needs.<br> It can fit loads of candles on the small definition screens. <br> It can even display one candle per one pixel column (see the last picture)

It's achieved by omitting popular candles frameworks <br> in need to decouple sizes of candles, sizes of their shadows, and sizes of spaces in between <br>⠀as well as ⠀ thickness of strokes — separatelly for body and shadows <br>⠀and at last ⠀ colors of all of those. <br> <br> In all candlestick libraries I used customisation did not allow such freedom like setting thickness/color of candle shadow separately from stroke of all candle which is WTH situation.

<img    src="210814sob062339 210807sob0808_forLineInPandas_df__number_of_candles scallerScalled_TkinterDisplayFullScreen ___PrzechwytWTrPełnoEkr.bmpPicasą_optimize=True.png"   >
<br> <br> <br> <br> 

### You just need ` binance_chart_tkinter.py ` file and data in ` *.csv. ` The program/script from ` *.py ` will use data from ` *.csv ` <br>



### If you don't see next charts you have too-high-density-screen xD

### 2px per candle ⠀+⠀ 1px per space
<img    src="210807sob0808 thickness_of_the_candle=2  thickness_of_the_shadow=2  spacing_of_the_candle=1 CROP .png"   > <br> <br>  <br> 
<img    src="220411pon1464.6 cX=thickness_of_the_candle=2 space=1 sh=1.00 +stroke=0 _ ChartWykres scallerScalled TkinterDisplayFullScreen.py.xcf.png"   >

<br> 

### 1px per candle ⠀+⠀ 1px per space
<img    src="210807sob0808 thickness_of_the_candle=1  thickness_of_the_shadow=1  spacing_of_the_candle=1 .png CROP .png"   >

### 2px per candle ⠀+⠀ 0px per space
<img    src="220411pon1464.5 cX=thickness_of_the_candle=1 space=1 sh=1.00 +stroke=1 _ ChartWykres scallerScalled TkinterDisplayFullScreen.py.xcf.png"   >

<br> <br> <br> 

### 1px per candle ⠀+⠀ 0px per space ⠀ ⠀ lighter
<img    src="210807sob0808 thickness_of_the_candle=1  thickness_of_the_shadow=1  spacing_of_the_candle=0 .png CROP .png"   >

### 1px per candle ⠀+⠀ 0px per space ⠀ ⠀ darker
<img    src="220411pon1464.4 cX=thickness_of_the_candle=1 space=0 sh=1.00 +stroke=0 _ ChartWykres scallerScalled TkinterDisplayFullScreen.py.xcf.png"   >

### 1px per candle ⠀+⠀ 0px per space ⠀ ⠀ but + 1px of body stroke <br> ⠀ — ⠀ so it's 2px candle every 1px of the screen

<img    src="220411pon1464.3 cX=thickness_of_the_candle=1 space=0 sh=1.00 +stroke=1 _ ChartWykres scallerScalled TkinterDisplayFullScreen.py.xcf.png"   >