# We will automate the Login page of Rediffmail Account
  # As the number of rows present in EXAMPLE keyword, Feature file will run those number of times

  Feature: SaveMail
    Scenario Outline: login data
      Given we navigate to Rediffmail account
      When we validate the username text
      And we type in the "<username>" edit box
      And we validate the password text
      And we type in the "<password>" field
      And we click on the sign in button
      Then we validate inbox page opens
      Given we click in write mail link
      When we fill the "<to>" field
      And we type the "<subject>" area
      And we click on the Bold button
      And we click on the Italic button
      And type in "<compose>" area
      And click on save button
      And Click on Draft Button
      And click on Delete Check Button
      And Click on Delete Button
      And we click on logout link
      Then we validate that we have logded out of rediffmail account
      Examples:
        | username | password |to | subject | compose |
        | selenium.testmay1999 | Dilee@123 | selenium.testmay2012@rediffmail.com | development | development done |



