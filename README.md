[![Build Status](https://travis-ci.com/dis09/statlib.svg?token=kXyCrK6nRFhWwsQDajhs&branch=master)](https://travis-ci.com/dis09/statlib)

# statlib

statistical functions in python - playground for the course *introduction to statistics with python*


## Development


On GitHub, fork the repository into your account by clicking on the `Fork` button.

Clone the forked repository
```
git clone https://github.com/<username>/statlib.git
```

Navigate to the root folder
```
cd statlib
```

Create a development branch and push it to your GitHub
```
git checkout -b dev
git push --set-upstream origin dev
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

On GitHub submit a `pull request` to merge your features from your `dev` branch into the original repository!

---


In case you need to update your master branch from the original upstream repository add the remote branch from the original repository to keep track of changes
```
git remote add upstream https://github.com/dis09/statlib.git 
git branch -va
```

Then update your master branch

```
git fetch upstream
git checkout master
git merge upstream/master
```

If you want to merge the master branch into your dev branch make

```
git checkout dev
git merge master 
```


## Package installation/ upgrade 

```
pip install git+https://github.com/dis09/statlib.git
pip install --upgrade git+https://github.com/dis09/statlib.git

```




