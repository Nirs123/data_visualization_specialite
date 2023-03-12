import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

#Function for bar Plot
def barPlot(data,year,classe,gender,location,locationName):
    #Configure values depending on gender
    if gender == "All":
        valuesGirls = list(data[0].values())
        valuesBoys = list(data[1].values())
        titles = list(data[0].keys())
        positions = range(len(valuesGirls))
    elif gender == "Girls":
        valuesGirls = list(data.values())
        titles = list(data.keys())
        positions = range(len(valuesGirls))
    elif gender == "Boys":
        valuesBoys = list(data.values())
        titles = list(data.keys())
        positions = range(len(valuesBoys))

    #Configure plot size and size settings
    width = 0.7
    fig = plt.figure(figsize=(8,6))

    #Plotting values depending on gender
    if gender == "All":
        plt.bar(positions,valuesBoys,width,color='#87CEEB')
        plt.bar(positions,valuesGirls,width,bottom=valuesBoys,color='#EC8993')
        plt.legend(labels=["Garçons","Filles"],fancybox=True,framealpha=0.7,borderpad=0.8,shadow=True)
    elif gender == "Girls":
        plt.bar(positions,valuesGirls,width,color='#EC8993')
    elif gender == "Boys":
        plt.bar(positions,valuesBoys,width,color='#87CEEB')

    #Adding title depending on location and year
    if location == "fr":
        plt.title(f"Nombre d'étudiants par spécialité en France \nen classe de {classe} à la rentrée {year}",size=14,pad=20)
    elif location == "region":
        plt.title(f"Nombre d'étudiants par spécialité dans la région de\n{locationName} en classe de {classe}\nà la rentrée {year}",size=13,pad=20)
    elif location == "academie":
        plt.title(f"Nombre d'étudiants par spécialité dans l'academie de\n{locationName} en classe de {classe}\nà la rentrée {year}",size=13,pad=20)
    
    #Adding other specifications
    plt.xticks(positions,titles,rotation=45,size=10)
    plt.xlabel("Spécialité",size=13)
    plt.ylabel("Nombre d'étudiants",size=13)
    plt.subplots_adjust(bottom=0.18,left=0.15,right=0.85,top=0.85)

    #Return plot
    return plt

def piePlot(data,year,classe,location,locationName,speName):
    #Configuring values
    values = [data[0][speName],data[1][speName]]
    labels = ["Filles","Garçons"]

    #Configuring plot
    plt.pie(values,colors=['#EC8993','#87CEEB'],autopct='%1.1f%%')
    plt.legend(labels=labels,fancybox=True,framealpha=0.7,borderpad=0.8,shadow=True)
    
    #Adding title depending on location and year
    if location == "fr":
        plt.title(f"Répartition des étudiants en {speName} en France \n en classe de {classe} à la rentrée {year}",size=14,pad=20)
    elif location == "region":
        plt.title(f"Répartition des étudiants en {speName} dans la région de\n{locationName} en classe de {classe}\nà la rentrée {year}",size=13,pad=20)
    elif location == "academie":
        plt.title(f"Répartition des étudiants en {speName} dans l'academie de\n{locationName} en classe de {classe}\nà la rentrée {year}",size=13,pad=20)
    
    #Adjust plot size
    plt.subplots_adjust(top=0.8)
    
    #Return plot
    return plt

def mapPlot(data,year,classe,location,speName):
    newDF = pd.DataFrame.from_dict(data)
    mapShape = gpd.read_file("geo/"+location+".geojson")

    if location == 'region':
        mapShape = mapShape[~mapShape['nom'].isin(['Guadeloupe',"Martinique","Guyane","Mayotte","La Réunion"])]

    mapShape = pd.merge(
        left=mapShape,
        right=newDF,
        left_on="code",
        right_on="index",
        how="left"
    )

    ax = mapShape.boundary.plot(edgecolor='black',linewidth=0.2,figsize=(8,7))
    mapShape.plot(ax=ax,column="value",cmap='Wistia',legend=True,legend_kwds={"shrink":0.7,
    "orientation":"vertical","format":"%.1f%%"})

    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)

    for edge in ['right','bottom','left','top']:
        ax.spines[edge].set_visible(False)

    if location == "dep":
        ax.set_title(f"Pourcentage des étudiants par département ayant\nla spécialité {speName} en {classe} a la rentrée {year}",
                    size=15,weight='bold',pad=15)
    else:
        ax.set_title(f"Pourcentage des étudiants par région ayant\nla spécialité {speName} en {classe} a la rentrée {year}",
                    size=15,weight='bold',pad=15)

    plt.subplots_adjust(
        top=0.805,
        bottom=0.12,
        left=0.16,
        right=0.93,
        hspace=0.2,
        wspace=0.2  
    )

    return plt