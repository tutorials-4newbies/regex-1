Regex Lesson 1
---

Binder for lesson 1:   
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tutorials-4newbies/regex-lessons/master?filepath=regex1.ipynb)

Tutorial at:
https://regexone.com/    
Try lessons 1 to 15 if you can    

   
   
Regex Lesson 2
---

Binder for lesson 2:   
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tutorials-4newbies/regex-lessons/master?filepath=regex2.ipynb)

### עבודה עצמית - בזוגות
#### Setup

Clone this repo to your pc   
```bash
 git clone https://github.com/tutorials-4newbies/regex-lessons.git
 ```

create a virtualenv and activate it   
**Windows**
```
python -m venv env
env\Scripts\activate
```

**Linux:** 
```bash
python -m venv env
source env/bin/activate
```

Install requirements inside the virtualenv 
```bash
pip install -r requirements.txt
```

#### תרגיל
יש כמה טסטים מוכנים מראש, צריך לעבוד על הקוד של הemail_validator.py

כדי לבדוק צריך להריץ את הטסטים    
``` pytest```   
 (inside the poject folder)