## happy path
* greet
  - utter_name
* name
  - utter_greet

## sad path 1
* greet
  - utter_name
* name
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_name
* name
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## New Story

* greet
  - utter_name
* name
  - utter_greet
* mood_great
    - utter_happy

## joke_story
* joke
  - utter_joke

## New Story

* joke
    - utter_joke
    - utter_did_that_help
* affirm
    - utter_goodbye
* goodbye
    - utter_goodbye

## New Story

* joke
    - utter_joke
* affirm
    - utter_goodbye

## New Story

* greet
  - utter_name
* name
  - utter_greet
* mood_great
    - utter_happy
* goodbye
    - utter_goodbye

## New Story

* greet
  - utter_name
* name
  - utter_greet
* name
    - utter_happy

## Story from conversation with me on May 27th 2019

* greet
  - utter_name
* name
  - utter_greet
* mood_great
    - utter_happy

## New Story

* joke
    - utter_joke
* affirm
    - utter_goodbye

## New Story

* greet
    - utter_name
* name
    - utter_greet

## New Story

* greet
    - utter_name
* name{"name":"raj"}
    - utter_greet
    - utter_goodbye
* goodbye

## New Story

* greet
    - utter_name
* name{"name":"robert"}
    - utter_greet
* mood_great
    - utter_goodbye

## New Story

* greet
    - utter_name
* name{"name":"rajesh"}
    - utter_greet
* mood_great
    - utter_goodbye

## Quote path
* greet
    - utter_name
* name{"name":"harsh"}
    - utter_greet
* requestquote
    - quote_form
    - form{"name":"quote_form"}
    - form{"name":null}
    - utter_send
* affirm
    - utter_goodbye

## New Story

* greet
    - utter_name
* name{"name":"raj"}
    - utter_greet
* mood_great
* requestquote
    - form{"name":"quote_form"}
    - form{"name":null}
    - utter_send
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_name
* name{"name":"harsh"}
    - utter_greet
* mood_great
* requestquote
    - form{"name":"quote_form"}
    - form{"name":null}

## New Story

* greet
    - utter_name
* name{"name":"harsh"}
    - utter_greet
* mood_great
* requestquote
    - quote_form
    - utter_send
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_name
* name
    - utter_greet
* mood_great
    - utter_domain
* consultance
    - utter_consultance
    - quote_form
    - utter_send
* goodbye
    - utter_goodbye
