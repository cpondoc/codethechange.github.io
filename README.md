## Deployment Note
Note that our `master` branch is actually our deployment branch, so the workflow involves checking out the `dev` branch. PR's should go into that branch.

## After cloning, to run dev server
```
yarn
yarn serve
```
## Compiles and minifies for production
```
yarn run build
```

## Deploy to production
```
./deploy.sh
```

### Lints and fixes files
```
yarn run lint
```