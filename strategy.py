
import pandas as pd

def run_hedge_strategy(spot_df, option_df):
    results = []

    for _, row in spot_df.iterrows():
        symbol = row['symbol']
        date = pd.to_datetime(row['date'])
        spot = row['spot']
        fut = row['futures']

        # Define hedge strikes
        call_strike = round(spot * 1.05, -1)
        put_strike = round(spot * 0.95, -1)

        # Match options for the symbol and date
        options = option_df[
            (option_df['symbol'] == symbol) &
            (pd.to_datetime(option_df['date']) == date)
        ]

        call_option = options[(options['strike'] == call_strike) & (options['type'] == 'CE')]
        put_option = options[(options['strike'] == put_strike) & (options['type'] == 'PE')]

        if not call_option.empty and not put_option.empty:
            ce_price = float(call_option['option_price'].values[0])
            pe_price = float(put_option['option_price'].values[0])

            pnl = pe_price - ce_price
            results.append({
                'symbol': symbol,
                'date': date.date(),
                'spot': spot,
                'futures': fut,
                'call_strike': call_strike,
                'put_strike': put_strike,
                'ce_price': ce_price,
                'pe_price': pe_price,
                'net_pnl': pnl
            })

    return pd.DataFrame(results)
