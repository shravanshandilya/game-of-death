from app import app
import os
from character import character

GoT_Followers = 1000000

#characters = {};
#char_file = open("char_data.txt","r")
#for char in char_file:
#	c = character(char,GoT_Followers)
#	characters[char.split(",")[0].replace(" ","_")]=c


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port,debug=True)
