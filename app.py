from flask import Flask, render_template
import Run_Spider
import Read_DB
import Draw_Plot

app = Flask(__name__, static_folder="statics")

@app.route("/")
def crawl_info():
    # Step 1: Runing Spider
    Run_Spider.run_spider()

    # Step 2 : Read Info 
    Info_dict = Read_DB.read_info()
    Coronavirus_Cases = Info_dict.get("Coronavirus_Cases")
    Death = Info_dict.get("Death")
    Recovered = Info_dict.get("Recovered")
    Table_Info = Info_dict.get("Table_Info")
    Country = Table_Info[0]
    TotalCases = Table_Info[1]
    NewCases = Table_Info[2]
    TotalDeath = Table_Info[3]
    NewDeath = Table_Info[4]
    TotalRecovered = Table_Info[5]
    ActiveCases = Table_Info[6]
    Serious_Critical = Table_Info[7]
    TotlaCase_in_1Mpop = Table_Info[8]

    # Step 3 : Get Plot Image
    Plot_Src = Draw_Plot.get_plot(Country, TotalCases)

    return render_template("index.html", Coronavirus_Cases=Coronavirus_Cases, Death=Death, Recovered=Recovered,
        Country=Country, TotalCases=TotalCases, NewCases=NewCases, TotalDeath=TotalDeath, NewDeath=NewDeath,
        TotalRecovered=TotalRecovered, ActiveCases=ActiveCases, Serious_Critical=Serious_Critical, TotlaCase_in_1Mpop=TotlaCase_in_1Mpop,
        Plot_Src=Plot_Src
    )
# Run app
app.run(debug=True)
