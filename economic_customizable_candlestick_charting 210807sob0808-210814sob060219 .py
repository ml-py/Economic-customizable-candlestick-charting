from  datetime  import  datetime,  timedelta
from  dateutil.relativedelta  import  relativedelta



import pandas as pd
df = pd.read_csv(   'H:\prog.py\prog moje\[PeterNistrup] Cryptocurrency Binance&Bitmex PythonAPIs .py\BTCUSDT-1m-data_fragm.csv'
                  , usecols=[ 'timestamp',  'open',  'high',  'low',  'close',  'volume'  ]
                  , index_col='timestamp',   parse_dates=True           )
print(  df.tail(10)  )
"""                     open      high       low     close     volume
timestamp                                                            
2021-07-16 15:03:00  31969.51  31981.52  31887.46  31916.89   76.968051
2021-07-16 15:04:00  31916.88  31916.88  31876.04  31898.75   36.691091
2021-07-16 15:05:00  31898.82  31916.42  31885.58  31891.00   30.792642
2021-07-16 15:06:00  31887.47  31898.98  31843.29  31871.41  284.763546
2021-07-16 15:07:00  31871.41  31887.22  31805.23  31813.70   75.813808

2021-07-16 15:08:00  31813.69  31844.89  31808.71  31828.99   40.603817
2021-07-16 15:09:00  31827.24  31827.24  31787.01  31795.74   51.856853
2021-07-16 15:10:00  31795.74  31831.17  31788.58  31831.17   30.916704
2021-07-16 15:11:00  31827.10  31899.99  31822.43  31888.60   62.264775
2021-07-16 15:12:00  31888.60  31909.44  31884.49  31893.41   25.112103 """
print(  df.shape  )
""" (666, 5) """



#                   fill_COLOR    tranparency_alpha    outline_color    outline_thickness
#        =     {   'fill':'#008000',  'alpha':.8,   'outline':'green3',  'width':1   }
FILL_uP  = dict(     fill='#008000',    alpha=.8,     outline='green3',    width=2   )
FILL_··  = dict(     fill='#808080',    alpha=.8,     outline='green3',    width=2   )
FILL_Do  = dict(     fill='#800000',    alpha=.8,     outline='red3'  ,    width=2   )
FILL_sh  = dict(     fill='#000000',    alpha=.25,    outline='white' ,    width=0   )
FILL_sh  = dict(     fill='#000000',    alpha=.25,    outline='pink'  ,    width=0   )

# vol_low  = dict(     fill='#000000',    alpha=.0,     outline='pink'  ,    width=2   )
vol_low  = dict(     fill='#000000',    alpha=.0,     outline='black' ,    width=1   )
# vol_low  = dict(     fill='#000000',    alpha=.0,     outline='blue1' ,    width=1   )
# vol_low  = dict(     fill='#000000',    alpha=.0,     outline='blue1' ,    width=1   )
# vol_low  = dict(     fill='#000000',    alpha=.0,     outline='SteelBlue', width=1   )
# vol_low  = dict(     fill='#000000',    alpha=.0,     outline='cyan' ,     width=1   )
# vol_low  = dict(     fill='#000000',    alpha=.0,     outline='yellow' ,   width=1   )

scrX  =  screen_pixels_x  =  1600
scrY  =  screen_pixels_y  =   900

MARGIN  =  2
VOLUME_FIELD_PART  =  0.3



cX   =  thickness_of_the_candle  =  4
sX   =  spacing_of_the_candle    =  3
cX_  =  thickness_of_the_shadow  =  4
# sX   =  spacing_of_the_candle    =  cX'#000000',    alpha=.8,     outline='black' ,    width=2   )
# FILL_Do  = dict(     fill='#800000',    alpha=.8,     outline='red3'  ,    width=2   )
sX_  =  spacing_of_the_shadow    =  3
# sX_  =  spacing_of_the_shadow    =  sX
number_of_candles  =   int(    scrX   /   (  cX  +  sX  )    )
print(   number_of_candles,   "   number_of_candles"   )

diff_half  =  half_of__cX_cXshadow_difference  =  int( (cX-cX) / 2 )
diff       =           cX_cXshadow             =        cX-cX

posX  =  int(  sX / 2  )
if  cX_ !=  cX:
    posX  =  posX  +  diff_half
    sX_  =  (cX+sX) - cX_



# big_bang  =  big_bang__start_of_history  =  0
world_end  =  end_of_known_data__could_be_now  =  df.shape[0]
user_imput  =  the_now_point__offset  =  offset_from_end_of_world  =  0
if  user_imput  >  df.shape[0]  -  1:
    user_imput                =  df.shape[0]  -  number_of_candles
    the_now_point__offset     =  df.shape[0]  -  number_of_candles
    offset_from_end_of_world  =  df.shape[0]  -  number_of_candles
print(   user_imput,   '  offset'   )

end___point  =  df.shape[0]  -  offset_from_end_of_world
start_point  =  end___point  -  number_of_candles
print(   f'{ start_point } ◆ { end___point } \t    start_point ◆ start_point'   )

if   start_point  <  0:
    print(   f""" ●◾·💥·◾●   BigBang - zero time point  in history  reached !!! !! !  !   !    !    !     !      !
start_point  set to zero = 0 """   )
    end___point  =  start_point  +  number_of_candles
    start_point  =  0
    print(   f'{ start_point } ◆ { end___point } \t    start_point ◆ start_point'   )
else                                      :
    end___point  =  df.shape[0]  -  offset_from_end_of_world
    start_point  =  end___point  -  number_of_candles
    print(   f'{ start_point } ◆ { end___point } \t    start_point ◆ start_point'   )

# if  end___point  >  df.shape[0]:       end___point  =  df.shape[0]
# if  end___point  >  df.shape[0]:
#     pass #   ~tk.draw()candle( x x x x color )  TIMER or sth
if  start_point  ==          0 :
    pass #   ~tk.draw()candle( x x x x color )  border
print(   f'{ start_point } ◆ { end___point } \t    start_point ◆ start_point'   )






import  tkinter  as  tk    # from  tkinter  import  Tk, Canvas   # from  tkinter  import  *
from  PIL  import  Image,  ImageTk

root  =  tk.Tk()

images = []  # to hold the newly created image
def create_rectangle(   x1, y1, x2, y2,  **kwargs   ):
    if 'alpha' in kwargs:
        alpha  =  int(   kwargs.pop( 'alpha' )  *  255   )
        fill  = kwargs.pop( 'fill' )
        fill  =  root.winfo_rgb( fill )  +  (alpha,)
        image =  Image.new(  'RGBA',   ( x2-x1, y2-y1 ),   fill  )
        images.append( ImageTk.PhotoImage( image ) )
        canvas.create_image(   x1, y1,   image=images[-1],   anchor='nw'   )
    canvas.create_rectangle(   x1, y1,  x2, y2,  **kwargs   )

w, h  =  root.winfo_screenwidth(),   root.winfo_screenheight()
root.overrideredirect(1); """ Instruct the window manager that the position of this widget   shall be defined 
                                by the user if WHO is "user", and by its own policy if WHO is  "program". """
root.geometry(  "%dx%d+0+0" % (w, h)  )
root.focus_set(); """Direct input focus to this widget.        If the application currently  does not have the focus
                   this widget will get the focus   if the application gets the focus through the window manager."""
root.bind(   "<Escape>",   lambda e:  e.widget.quit()   )
# canvas  =  Canvas(  width=300,  height=200,   background='black'  )
canvas  =  tk.Canvas(  width=w,  height=h,   background='white'  )
canvas.pack()






volume_screen_size  =   int(   h * VOLUME_FIELD_PART   )

volume_field_h_min   =  h - MARGIN
volume_field_h_MAX   =  h - MARGIN  -  volume_screen_size
candle_field_h_min   =  h - MARGIN  -  volume_screen_size  -  MARGIN
candle_field_h_MAX   =  0 + MARGIN

real_max  =  df.iloc[  start_point : end___point  ,    : 4  ].max().max()
real_min  =  df.iloc[  start_point : end___point  ,    : 4  ].min().min()
vol__max  =  df.iloc[  start_point : end___point  ,  4      ].max()
print(   f'  real_max   real_min   vol__max  {   real_max,  real_min,  vol__max   }'   )


# persentage  =  ( real_max - real_min )  /  ( real_max - real_min )
def  scale(   real_number,   real_min,   real_MAX,   field_MAX,   field_min   ):

    scalled  =    ( (  real_number - real_min  )/(  real_MAX - real_min  ) )    \
                * (  field_MAX - field_min  )                                     \
                + field_min
    # print(   real_number,   '   -->   ',   scalled   )
    scalled  =  round( scalled )
    # print(   real_number,   '   -->   ',   scalled   )
    return  scalled




# ### FOR SPEED TEST
# for   index, row   in   df.head(  start_point+number_of_candles   )\
#                           .tail(              number_of_candles   )\
#                           .iterrows():#     print(   index,   * row   ,sep=' \t'   )

pointer_helper  =  start_point
for   index, row   in   df.iloc[  start_point  :  end___point  ]\
                          .iterrows():

    # print(   index,   * row,                                          sep=' \t◾'    )
    """ 2021-07-16 15:12:00 	◾31888.6 	◾31909.44 	◾31884.49 	◾31893.41 	◾25.112103 """
    # print(   index,     row[0],  row[1],  row[2],  row[3],  row[4],   sep='  ◾  '   )
    """ 2021-07-16 15:12:00  ◾  31888.6  ◾  31909.44  ◾  31884.49  ◾  31893.41  ◾  25.112103 """
    posY_o  =      int( round( scale(    row[0],    real_min,  real_max,    candle_field_h_min,  candle_field_h_MAX   ) ) )
    posY_h  =      int( round( scale(    row[1],    real_min,  real_max,    candle_field_h_min,  candle_field_h_MAX   ) ) )
    posY_l  =      int( round( scale(    row[2],    real_min,  real_max,    candle_field_h_min,  candle_field_h_MAX   ) ) )
    posY_c  =      int( round( scale(    row[3],    real_min,  real_max,    candle_field_h_min,  candle_field_h_MAX   ) ) )
    # print  #559.0   ( round( scale(    row[3],    real_min,  real_max,    candle_field_h_min,  candle_field_h_MAX   ) ) )
    posY_V  =      int( round( scale(    row[4],           0,  vol__max,    volume_field_h_MAX,  volume_field_h_min   ) ) )
    """ 350 350 260 261 """
    # posY_o  =  h - int( round( scale(    row[0],    candle_field_h_min,  candle_field_h_MAX   ) ) )
    # posY_h  =  h - int( round( scale(    row[1],    candle_field_h_min,  candle_field_h_MAX   ) ) )
    # posY_l  =  h - int( round( scale(    row[2],    candle_field_h_min,  candle_field_h_MAX   ) ) )
    # posY_c  =  h - int( round( scale(    row[3],    candle_field_h_min,  candle_field_h_MAX   ) ) )
    # posY_V  =  h - int( round( scale(    row[4],           0,  vol__max,    volume_field_h_MAX,  volume_field_h_min   ) ) )

    # print(   posY_o,   posY_h,   posY_l,   posY_c,   posY_V   )
    """ 550 550 640 639         ,a vol zadziałał   leczJużNaInnejSkali         """
    """ ValueError: Width and height must be >= 0    -  WTF                    """







    #                                        inclusive
    # print( '  ◾◾◾ ',          * df.iloc[  start_point -0  ]   ,   sep='  ◾  '   )
    # print( '  ◾◾◾ ',   index,   df.iloc[  start_point -0  ][4],   sep='  ◾  '   )
    # print( '  ◾◾◾ ',          * df.iloc[  end___point -1  ]   ,   sep='  ◾  '   ) # inclusive
    # print(   ◾◾◾ ',   index,   df.iloc[  end___point -1  ][4],   sep='  ◾  '   ) # inclusive
    """         ◾◾◾   ◾  31395.98  ◾  31395.98  ◾  31293.48  ◾  31294.9  ◾  51.100544
                ◾◾◾   ◾  2021-07-16 10:47:00                              ◾  51.100544
                ◾◾◾   ◾  31888.6  ◾  31909.44  ◾  31884.49  ◾  31893.41  ◾  25.112103
                ◾◾◾   ◾  2021-07-16 10:47:00                              ◾  25.112103              """
    # print(   '  ◆◆◆ ',   index           ,   type( index            ),   sep='  ◆  '   )
    # print(   '  ◆◆◆ ',   index.__repr__(),   type( index.__repr__() ),   sep='  ◆  '   )
    """         ◆◆◆   ◆  2021-07-16 10:47:00  ◆  <class 'pandas._libs.tslibs.timestamps.Timestamp'> """
    """         ◆◆◆   ◆  Timestamp('2021-07-16 10:47:00')  ◆  <class 'str'>                         """








    # print(   index.to_timestamp()   )
    """ AttributeError: 'Timestamp' object has no attribute 'to_timestamp' """
    # print(   index - datetime.timestamp( timedelta( 60 ) ) ,   row[4],    )    #
    # print(   index - relativedelta(seconds=60.0),   row[4],    )    #
    # print(   pd.Timedelta(  '15 seconds'  ),    pd.Timedelta(  '15 seconds'  ).__repr__()    )
    """      0 days 00:00:15                       Timedelta( '0 days 00:00:15' )            """

    # print(   pd.offsets.Second( 2 ),             type( pd.offsets.Second( 2 ) )   )
    """      <2 * Seconds>    <class 'pandas._libs.tslibs.offsets.Second'>        """
    # print(   df.iloc[   index  -  pd.offsets.Second( 2 )                    ]   )
    """ TypeError: Cannot index by location index with a non-integer key          """
    # print(   df.iloc[   index  -  pd.offsets.Second( 2 ).astype( int )      ]   )
    """ AttributeError: 'pandas._libs.tslibs.offsets.Second' object has no attribute 'astype' """



    # import  numpy  as  np    # Convert TimeDelta column (5 days etc.) into an integer column (5)
    # df['timeDelta']  =  ( df['timeDelta']  /  np.timedelta64( 1, 'D' )    ).astype( int )
    # df.timeDelta     =  ( df .timeDelta    /  np.timedelta64( 1, 'D' )    ).astype( int )
    """
    How to access previous row while iterating through rows in Pandas DataFrame?

    Hi, I’ want to  add / subtract  from  <class 'pandas._libs.tslibs.timestamps.Timestamp'>  some amount of time (in my case 1 minute) and do it a few times, to compare certain values across rows previous rows. I imagine that the code should looks like this
    for   index, row   in   df.iloc[  start_point  :  end___point  ].iterrows():
        # do some normal stuff
        print(   index,   * row   ,sep=' \t'   )
        # try to look into the past
        one_min = 60
        if       df.iloc[ index ][0]  <  df.iloc[ index - one_min     ][0] \
            and  df.iloc[ index ][0]  <  df.iloc[ index – one_min * 2 ][0]:
            do_sth()

    first – the index of DataFrame is  some_time_stamp   so I can not access it with a int index.
    Than I wonder to subtract  1_min  from the  index of DataFrame. I tried it by
    pd.Timedelta()
    pd.offsets.Second()
    df.timeDelta and np.timedelta64()
    and did not succeed
    What could be the way to do that?
    """






    # import  numpy   as  np
    # TimedeltaIndex_5_sztuk  =  pd.to_timedelta(  np.arange(5),  unit="s"  )
    # # print(   df.iloc[   index - TimedeltaIndex_5_sztuk[1]   ]   )
    """ TypeError: Cannot index by location index with a non-integer key """

    # print(   index.to_ti(),   row[4],    )    # Timestamp('2021-07-16 10:47:00') 51.100544

    # print(   df.iloc[   index - timedelta( seconds=60 )   ]   )
    # print(   df.iloc[   index - timedelta( minutes=1 )   ]   )
    """ TypeError: Cannot index by location index with a non-integer key """
    # print(   index-1,   row,    )
    """ TypeError: Addition/subtraction of integers and integer-arrays with Timestamp
    is no longer supported.  Instead of adding/subtracting `n`, use `n * obj.freq`    """



    ###  S H A D  O W
    # create_rectangle(   posX,  posY_l,    posX+cX,  posY_h,   fill=FILL_sh,  alpha=.2,   width=0   )
    create_rectangle(   posX,  posY_l,    posX+cX,  posY_h,   **FILL_sh   )

    if  row[0]  <   row[3]:    ###   UP  Candlestick
        create_rectangle(   posX,  posY_o,    posX+cX,  posY_c            ,   **FILL_Do   )
        create_rectangle(   posX,  posY_V,    posX+cX,  volume_field_h_min,   **FILL_Do   )
    if  row[0]  ==  row[3]:    ###  Doji Candlestick
        create_rectangle(   posX,  posY_o,    posX+cX,  posY_c            ,   **FILL_··   )
        create_rectangle(   posX,  posY_V,    posX+cX,  volume_field_h_min,   **FILL_··   )
    if  row[0]  >   row[3]:    ###  DOWN Candlestick              fill='#008000',  alpha=1 ,   'outline':"red",   width=0
        create_rectangle(   posX,  posY_c,    posX+cX,  posY_o            ,   **FILL_uP   )
        create_rectangle(   posX,  posY_V,    posX+cX,  volume_field_h_min,   **FILL_uP   )
        # create_rectangle(   posX,  posY_V,    posX+cX,  volume_field_h_min,   **FILL_uP,   **OUT_vol   )

    ###  V O L U M E N

    """                                                          ⇚ ⇜ ← ⇐ ⇠ ⇦ ↢ ↤ ↞   ➨  ➜  ➽  ❰  ❱  """
    # print(   '  ⇐  previous ',   * df.iloc[  pointer_helper - 1  ]   ,sep='  ⇐  '   )
    if          df.iloc[  pointer_helper  ][4]  <  df.iloc[  pointer_helper - 2  ][4]\
          and   df.iloc[  pointer_helper  ][4]  <  df.iloc[  pointer_helper - 1  ][4]:
        create_rectangle(   posX,  posY_V,    posX+cX,  volume_field_h_min,   **vol_low   )
    pointer_helper  +=  1




    posX  +=  sX + cX

window = tk.Toplevel(root)
window.geometry(  "100x100"  )  # Whatever size
window.overrideredirect(1)  # Remove border
# root.attributes(   '-alpha',  0.0   )  # For icon   ### nie pokazuje okna wcale,  acz jest
# root.attributes(   '-alpha',  0.5   )  # For icon   ### pokazuje okno przezroczyste  screenShoty Sie nie robą wcale
root.mainloop( )  # root.mainloop( 0 )