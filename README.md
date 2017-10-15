# ProgrammingContestApi

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/499937200761438582779f2a28b58166)](https://www.codacy.com/app/uzumaki-narut0/ProgrammingContestApi?utm_source=github.com&utm_medium=referral&utm_content=uzumaki-narut0/ProgrammingContestApi&utm_campaign=badger)
[![Travis CI Badge](https://travis-ci.org/uzumaki-narut0/ProgrammingContestApi.svg?branch=master)](https://travis-ci.org/uzumaki-narut0/ProgrammingContestApi)

A restful API constructed using flask_restful which returns all ongoing and upcoming programming contests in JSON.

**Fetch Contest Details**
----
  Returns json data about upcoming and ongoing programming contests on various platforms like Codechef, Codeforces and Hackerearth.

* **URL**

  https://tranquil-caverns-50595.herokuapp.com/

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"result": {"present_contests": [{"end_time": "2018-01-05 00:00:00", "name": "ZCO Practice Contest", "code": "ZCOPRAC", "start_time": "2015-11-05 00:00:00", "platform": "codechef", "contest_url": "www.codechef.com/ZCOPRAC"}], "upcoming_contests": [{"end_time": "2017-10-16 13:05:00", "name": "Codeforces Round #441 (Div. 1, by Moscow Team Olympiad)", "code": 875, "start_time": "2017-10-16 11:05:00", "platform": "codeforces", "contest_url": "http://codeforces.com/contest/875"}]}}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
  
* **Sample Call:**

  ```javascript
    $.ajax({
      url: "https://tranquil-caverns-50595.herokuapp.com",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
