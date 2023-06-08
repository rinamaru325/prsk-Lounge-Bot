#ID of your updating spreadsheet, can be found by copying
#the part after /d/ in the sheet link
SH_KEY = '1QGkQxiYncQBEyIxU049DUGA3QR0bP2JuHfenZrlVB6E'

LOOKUP_KEY = '1ts17B2k8Hv5wnHB-4kCE3PNFL1EXEJ01lx-s8zPpECE'

# first item is where the names go,
# second is where the placements go,
# third is where the multipliers go
updateCols = ["C", "B", "A"]

# the first item is the starting column,
# the second is the ending column
# (the total number of columns gotten
#  should be 7, including these two)
getCols = ["D", "J"]

#A1 notation of the column that Peak MMRs are stored in Player History
peakColumn = "C"

#rowOffset is = (row number of first player on Player History - 1)
#colOffset is = first Match History column on Player History
#               (column H for 150cc lounge, which is the 8th column)
rowOffset = 1
colOffset = 8

#the top row on the bot sheet to fill in for each format
sheet_start_rows = {1: 4,
                    2: 19,
                    3: 34,
                    4: 49,
                    6: 64}
#the top row on the MMR tables xlsx file to fill in for each format
table_start_rows = {1: 6,
                    2: 22,
                    3: 43,
                    4: 62,
                    6: 80}

#first value is where the name goes, second is where the penalty amount goes
pen_cells = ["C80", "D80"]
pen_cols = [3, 4]
pen_row = 80
#first cell is the start of the range, second is end of the range
get_strike_info = ["E80", "M80"]

bot_channels = [741906846209671223]

#id of the results channels for each tier
channels = {"X": 1113581009439571968,
            "A": 1096433776235642880,
            "B": 1113580344084537405,
            "C": 1113580381418041405,
            "D": 1113581044126470267}

#contains the emoji ID and role ID for each rank in the server;
#rank names should match up with getRank function below
ranks = {
    "Grandmaster": {
        "emoji": "<:GrandMaster:1107296609659789353>",
        "roleid": 1113225109029789807},
    "Master": {
        "emoji": "<:Master:1107296600633639012>",
        "roleid": 1113225106924244993},
    "Diamond 2": {
        "emoji": "<:Diamond:1107296605415161948> 2",
        "roleid": 1113225080999260231},
    "Diamond 1": {
        "emoji": "<:Diamond:1107296605415161948> 1",
        "roleid": 1113225077920632892},
    "Ruby 2": {
        "emoji": "<:Ruby:1107296613535334452> 2",
        "roleid": 1113225082207211620},
    "Ruby 1": {
        "emoji": "<:Ruby:1107296613535334452> 1",
        "roleid": 1113225089664700509},
    "Sapphire 2": {
        "emoji": "<:Sapphire:1107296631285628988> 2",
        "roleid": 1113225091367583786},
    "Sapphire 1": {
        "emoji": "<:Sapphire:1107296631285628988> 1",
        "roleid": 1113225093733167275},
    "Platinum 2": {
        "emoji": "<:Platinum:1107296634984996984> 2",
        "roleid": 1113225095616397342},
    "Platinum 1": {
        "emoji": "<:Platinum:1107296634984996984> 1",
        "roleid": 1113225100586663997},
    "Gold 2": {
        "emoji": "<:Gold:1107296620531425370> 2",
        "roleid": 1113225102562185258},
    "Gold 1": {
        "emoji": "<:Gold:1107296620531425370> 1",
        "roleid": 1113225104898404482},
    "Silver 2": {
        "emoji": "<:Silver:1107296627426873364> 2",
        "roleid": 1113225947123040286},
    "Silver 1": {
        "emoji": "<:Silver:1107296627426873364> 1",
        "roleid": 1113225949639606353},
    "Bronze 2": {
        "emoji": "<:Bronze:1107296624331472947> 2",
        "roleid": 1113225951099232406},
    "Bronze 1": {
        "emoji": "<:Bronze:1107296624331472947> 1",
        "roleid": 1113226042329534566},
    "Iron 2": {
        "emoji": "<:Iron:1107296616018362529> 2",
        "roleid": 1113224869694427167},
    "Iron 1": {
        "emoji": "<:Iron:1107296616018362529> 1",
        "roleid": 1113224440231235644}
    }

place_MMRs = {"bronze": 2500,
              "iron": 1500}

#this is where you define the MMR thresholds for each rank
def getRank(mmr: int):
    if mmr >= 17000:
        return("Grandmaster")
    elif mmr >= 16000:
        return("Master")
    elif mmr >= 15000:
        return("Diamond 2")
    elif mmr >= 14000:
        return("Diamond 1")
    elif mmr >= 13000:
        return("Ruby 2")
    elif mmr >= 12000:
        return("Ruby 1")
    elif mmr >= 11000:
        return("Sapphire 2")
    elif mmr >= 10000:
        return("Sapphire 1")
    elif mmr >= 9000:
        return("Platinum 2")
    elif mmr >= 8000:
        return("Gold 2")
    elif mmr >= 7000:
        return("Gold 1")
    elif mmr >= 6000:
        return("Silver 2")
    elif mmr >= 5000:
        return("Silver 1")
    elif mmr >= 4000:
        return("Bronze 2")
    elif mmr >= 3000:
        return("Bronze 1")
    elif mmr >= 2000:
        return("Iron 2")
    else:
        return ("Iron 1")

#ignore if end user
#taken from gspread.utils:
#https://github.com/burnash/gspread/blob/master/gspread/utils.py
def rowcol_to_a1(row, col):
    row = int(row)
    col = int(col)

    div = col
    column_label = ''

    while div:
        (div, mod) = divmod(div, 26)
        if mod == 0:
            mod = 26
            div -= 1
        column_label = chr(mod + 64) + column_label

    label = '%s%s' % (column_label, row)

    return label

