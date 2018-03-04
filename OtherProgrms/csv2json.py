import csv
import json

''' Approach - 1 -  Using CSV and JSON libraries'''

#---------------------------------------------------------------------------------------#
csvfile = open('/Users/mbhekne/Desktop/ExploreInnov/csv2jsonfiles/AXC_LC.csv', 'r')
jsonfile = open('/Users/mbhekne/Desktop/ExploreInnov/csv2jsonfiles/AXC_LC.json', 'w')

#fieldnames = ("Loan_ID","Gender","Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area","Loan_Status")
#fieldnames=("post_id","subject","details","user_id","community_id","answers_count","comments_count","bookmarks_count","up_votes_count","down_votes_count","type","contextual_id","created_at","updated_at","legacy_id","discussion_replies_count","product_id","details_raw","recommended_answer_id","last_activity_at","image_attachments_count","announcement_updates_count","cached_question_tag_list","recommended_by_user_id","flags_count","is_closed","state","akismet_spam","locale","authored_at","modified_at","published_at","content_identifier","author_id","author_type")
fieldnames=("PRODUCT_ID","INTUIT_ITEM_CODE","PRODUCT_DESCRIPTION","PRODUCT_FAMILY_DESCRIPTION","PRODUCT_EDITION_DESCRIPTION","PRODUCT_VERSION_CODE","PRODUCT_ROLLUP","PRODUCT_ROLLUP_ID","BATCH_EVENT_ID","CREATED_TIMESTAMP","UPDATED_TIMESTAMP")

reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
#---------------------------------------------------------------------------------------#


'''
Approach - 2 -  Using CSV Mapper
import csvmapper

fields = ("Loan_ID","Gender","Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area","Loan_Status")
parser = csvmapper.CSVParser('/Users/mbhekne/Desktop/ExploreInnov/csv2jsonfiles/CSVFile.csv', csvmapper.FieldMapper(fields))

converter = csvmapper.JSONConverter(parser)

print converter.doConvert(pretty=True)
#---------------------------------------------------------------------------------------#

'''