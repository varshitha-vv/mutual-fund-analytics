import requests
import pandas as pd

scheme_codes = [
    125497,
    120503,
    120716,
    118834,
    120828,
    119551
]

for scheme in scheme_codes:

    print(f"\nFetching Scheme: {scheme}")

    url = f"https://api.mfapi.in/mf/{scheme}"

    response = requests.get(url)

    if response.status_code == 200:

        nav_data = response.json()

        nav_df = pd.DataFrame(nav_data["data"])

        output_file = f"data/raw/live_nav_{scheme}.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

    else:

        print(f"Failed to fetch Scheme {scheme}")