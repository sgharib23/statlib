[![Build Status](https://travis-ci.com/dis09/statlib.svg?token=kXyCrK6nRFhWwsQDajhs&branch=master)](https://travis-ci.com/dis09/statlib)

# statlib

statistical functions in python - playground for the course *introduction to statistics with python*


## Development


Clone the repository
```
git clone https://github.com/dis09/statlib.git
```

Navigate to the root folder
```
cd statlib
```

Create a feature branch and push it to GitHub
```
git checkout -b [name_of_your_new_branch]
git push --set-upstream origin [name_of_your_new_branch]
```

Make changes to the code and test it with 
```
python -m pytest
```

Push your changes to your feature branch

```
git add .
git commit -m "add feature x"
git push
```


In case you need to update your feature branch from the master branch make

```
git checkout master
git pull
git checkout [name_of_your_new_branch]
git merge master 
git push
```


## Package installation/ upgrade 

```
pip install git+https://github.com/dis09/statlib.git
pip install --upgrade git+https://github.com/dis09/statlib.git

```




