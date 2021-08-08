# API /coins/single

All information about a single coin at latest moment in time.

curl -X POST 'https://api.livecoinwatch.com/coins/single' \
  -H 'content-type: application/json' \
  -H 'x-api-key: <YOUR_API_KEY>' \
  -d '{"currency":"USD","code":"ETH","meta":true}'
Let's see all of current data on ETH, in USD currency:

# Example :
  '''json
  {
    "name": "Ethereum",
    "symbol": "Ξ",
    "color": "#282a2a",
    "png32": "https://lcw.nyc3.cdn.digitaloceanspaces.com/production/currencies/32/eth.png",
    "png64": "https://lcw.nyc3.cdn.digitaloceanspaces.com/production/currencies/64/eth.png",
    "webp32": "https://lcw.nyc3.cdn.digitaloceanspaces.com/production/currencies/32/eth.webp",
    "webp64": "https://lcw.nyc3.cdn.digitaloceanspaces.com/production/currencies/64/eth.webp",
    "exchanges": 153,
    "markets": 3717,
    "pairs": 1773,
    "allTimeHighUSD": 2036.3088032624153,
    "circulatingSupply": 115250583,
    "totalSupply": null,
    "maxSupply": null,
    "rate": 1786.6742250505124,
    "volume": 11522748696,
    "cap": 205915246068
  }
# Request
## key	type	description
### currency	
- string	any valid coin or fiat code
### code	
- string	coin code
### meta	
- boolean	to include full coin information or not
# Response
## key	type	description
|  name  |  type |  description  |
|--------|-------|---------------|
|  name  |  string  | 	coin's name  |
|  symbol  | string | coin's symbol  |
|color|	string	|hexadecimal color code (#282a2a)|
|png32|	string	|32-pixel png image of coin icon||
|png64|	string	|64-pixel png image of coin icon|
|webp32|	string	|32-pixel webp image of coin icon|
|webp64	|string	|64-pixel webpg image of coin icon|
|exchanges	|number|	number of exchange coin is present at|
|markets	|number	|number of markets coin is present at|
|pairs	|number|	number of unique markets coin is present at|
|allTimeHighUSD	|number|	all-time high in USD|
|circulatingSupply	|number|	number of coins minted, but not locked|
|totalSupply	|number|	number of coins minted, including locked|
|maxSupply|	number|	maximum number of coins that can be minted|
|rate	|number|	price of coin in requested currency|
|volume	|number|	reported trading volume of the coin in last 24 hours in requested currency|
|cap|	number	|coin's market cap in requested currency|
|totalCap	|number|	coin's hypothetical total capitalization at the moment|
