from flask import Flask, render_template, request, redirect,url_for
import sqlite3

app = Flask(__name__, template_folder="templates", static_folder="static")

ALLOWED_POKEMON = ['Bulbasaur','Squirtle','Charmander', 'Pikachu', 'Mewtwo']
ADVENTURERS_DICT = {}

@app.route("/")
def start_fn():
        return render_template("start.html", 
                               SERVER_MSG = "Choose A Pokemon!",
                               ALLOWED_POKEMON = ALLOWED_POKEMON)

@app.route("/chosen", methods=["GET","POST"])
def chosen_fn():
    print(request.method)
    if request.method == "POST": # add posted data, keys: 'NAME', 'POKEMON'
        ## v1: add to python dict | ## v2: add to sqlite db |## v3: v1 vs v2
        posted_form_dict = request.form
        if "NAME" not in posted_form_dict:
            return render_template("error.html", SERVER_MSG = 'ERROR: NAME IS MISSING')
        elif "POKEMON" not in posted_form_dict:
            return render_template("error.html", SERVER_MSG = 'ERROR: POKEMON NOT SELECTED!')
        elif posted_form_dict["POKEMON"] not in ALLOWED_POKEMON:
            return render_template("error.html", SERVER_MSG = 'ERROR: ILLEGAL POKEMON SELECTED!')
        else:
            name = posted_form_dict["NAME"]         # get hero name
            pokemon = posted_form_dict["POKEMON"]   # get hero pokemon
        
            ADVENTURERS_DICT[name]=pokemon # add hero & their pokemon to db
            
            ########## beg add-to-db
            con = sqlite3.connect("pokemon.db")
            with con:
                cur = con.cursor()    
                
            #     res = cur.execute("SELECT * FROM adventurers").fetchall()
            #     print(res)
                
            #     con.execute("INSERT INTO adventurers (name, pokemon) VALUES ('ash','bulba')")
            #     con.execute("INSERT INTO adventurers (name, pokemon) VALUES (?,?)", ('misty','squirt squirt'))    
            #     con.executemany("INSERT INTO adventurers (name, pokemon) VALUES (?,?)", INPUT_LIST)    
                con.execute("INSERT INTO adventurers (name, pokemon) VALUES (?,?)", (name,pokemon))    
                
                # res = cur.execute("SELECT * FROM adventurers").fetchall()
                # print(f"\n6. Insert Test Data:")
                # [print(f"\t\t{r}") for r in res]
                
            ########## end add-to-db
            
            print(ADVENTURERS_DICT)
            return render_template("chosen.html", SERVER_MSG = f"{name.capitalize()} Chose {pokemon}!")
    return redirect("/")

@app.route("/adventurers_list")
def adventurers_list_fn():
    con = sqlite3.connect("pokemon.db")
    with con:
        cur = con.cursor()    
        ADVENTURERS_LIST = cur.execute("SELECT * FROM adventurers").fetchall()
        print(f"select*fromadv_type: {type(ADVENTURERS_LIST)}")
        [print(f"\t\t{r}") for r in ADVENTURERS_LIST]
        
        # print(ADVENTURERS_DICT)
    
    return render_template("adventurers_list.html", 
                           SERVER_MSG = "Adventurers List",
                           ADVENTURERS_LIST = ADVENTURERS_LIST)
                        #    ADVENTURERS_DICT = ADVENTURERS_DICT)
            # (1, 'ash', 'Bulbasaur', None)
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000,debug=True)
