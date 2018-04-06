## Inisght Data Engineering - Coding Challenge

<pre>
├── input
│   └── README.md
├── insight_testsuite
│   ├── run_tests.sh
│   └── tests
│       └── test_1
│           ├── input
│           │   ├── inactivity_period.txt
│           │   └── log.csv
│           ├── output
│           │   └── sessionization.txt
│           └── README.md
├── output
│   └── README.md
├── README.md
├── run.sh
└── src
    ├── README.md
    ├── sessionization.py
    ├── session.py
    ├── test
    │   ├── test_session.py
    │   └── test_utils.py
    └── utils.py
</pre>

* **session.py** - A session class for storing related information of a session
* **utils.py** - Contains utility functions
* **sessionization.py** - Main logic for processing log data
* test
    * **test_session.py** - unit test for session class
    * **test_utils.py** - unit test for utility functions
