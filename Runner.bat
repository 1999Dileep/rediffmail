cd C:\Users\HP\Desktop\automation\RediffMail

behave -f allure_behave.formatter:AllureFormatter -o ./Reports ./features
behave --junit --junit-directory my_report features/ScenarioOutlineExample.feature
behave -f json.pretty -o JSON_REPORTS features/ScenarioOutlineExample.feature