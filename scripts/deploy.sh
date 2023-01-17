ENV=${1:-dev}
CURRENT=$(pwd)

# init test
cd ../lambdas/events_processor/src/tests
pytest
cd ../../../../

# build
sam build

# e2e test
for f in lambdas/events_processor/src/tests/events/*.json; do sam local invoke --event $f EventsProcessorFunction; done

# deploy
sam deploy --config-env $ENV --no-confirm-changeset

cd $CURRENT