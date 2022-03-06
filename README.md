# DataBootcamp_Project4
The above notebooks need to be run in colab after downloading the repository in your google drive root directory

/
Project4.odp    - Slides for the flow and the challenges faced

/code - contains the various jupyter notebooks and the various ML models

/data - contains the data used and created

/code/

scrape_height_weight.ipynb - colab trial notebook to test the scraping code on specific records

scrape.py - python script to do batch scraping for 10000 records at a time

scrape_err_recs.py - python script to scrape the errored records using alternate strategies

scrape_2021_recs.py - python script to scrape the recs for the 2022 year

Project4_scrape-1.ipynb - colab notebook used to get the datafiles from github and then run the batch python scraping files

predict_drafts.ipynb - colab notebook that has  the ML code for predicting the draftpicks


/data

Group6_Project_data.csv - original data file fetched from kaggle contains stats for various NCAA players over the last 12 years

CollegeBasketballPlayers2022.csv - players in the NCAA 2022 season with their stats to be used for predicting their chances to NBA draft

player_add_info*.csv - data files containing the scraped data for position height weight for various batches

Draft_picks_precision_cw.csv - draft pick predictions picked using the class weights 
                                and who have a probability higher than mean+.5*std_dev

merged_data_file.csv - data file after merging height and weight data into the original file

combined_data_set.csv - data file after we combined both pre-2022 and post-2022 data

## Presentation ##
[basketball_project4.pptx](https://github.com/AvondreHenderson/DataBootcamp_Project4/files/8191316/basketball_project4.pptx)

