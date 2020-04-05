import scrapy 
import pickle 

class mySoider(scrapy.Spider):
    name = "coronaCrawler" #name of your spider

    def start_requests(self):
        page_url = ['https://www.worldometers.info/coronavirus/']

        for url in page_url:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        tmp_list = response.xpath("//div[@class='maincounter-number']/span/text()").extract()
        Coronavirus_Cases = tmp_list[0]
        Death = tmp_list[1]
        Recovered = tmp_list[2]

        number_of_country = len(response.xpath("//tbody/tr/td[2]/text()").extract())
        Table_Info = []
        Country = []

        for i in range(1, number_of_country):
            this_country = response.xpath("//tbody/tr["+ str(i) +"]/td[1]/text()").extract()
            self.delete_key_from_list(this_country, " ")
            if this_country == []:
                this_country = response.xpath("//tbody/tr["+ str(i) +"]/td[1]/a/text()").extract()
                if this_country == []:
                    this_country = response.xpath("//tbody/tr["+ str(i) +"]/td[1]/span/text()").extract()
            self.delete_key_from_list(this_country, " ")
            if this_country == []:
                this_country.append("")
            Country.append(this_country[0])

        self.delete_key_from_list(Country, "")
        print("Number of Countries : ", len(Country))
        
        TotalCases = response.xpath("//tbody/tr/td[2]/text()").extract()
        NewCases = response.xpath("//tbody/tr/td[3]/text()").extract()
        TotalDeath = response.xpath("//tbody/tr/td[4]/text()").extract()
        NewDeath = response.xpath("//tbody/tr/td[5]/text()").extract()
        TotalRecovered = response.xpath("//tbody/tr/td[6]/text()").extract()
        ActiveCases = response.xpath("//tbody/tr/td[7]/text()").extract()
        Serious_Critical = response.xpath("//tbody/tr/td[8]/text()").extract()
        TotlaCase_in_1Mpop = response.xpath("//tbody/tr/td[9]/text()").extract()

        Table_Info.append(Country)
        Table_Info.append(TotalCases)
        Table_Info.append(NewCases)
        Table_Info.append(TotalDeath)
        Table_Info.append(NewDeath)
        Table_Info.append(TotalRecovered)
        Table_Info.append(ActiveCases)
        Table_Info.append(Serious_Critical)
        Table_Info.append(TotlaCase_in_1Mpop)

        f = open("statics/DB/CoronaDB.dat", "wb")
        pickle.dump(Coronavirus_Cases, f)
        pickle.dump(Death, f)
        pickle.dump(Recovered, f)
        pickle.dump(Table_Info, f)
        f.close()

    def delete_key_from_list(self, mylist, key):
        while key in mylist:
            mylist.remove(key)
        return mylist