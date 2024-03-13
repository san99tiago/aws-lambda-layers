# External imports
import pytest
import aws_cdk as core
import aws_cdk.assertions as assertions

# Own imports
from cdk.stacks.cdk_lambda_layers_stack import LambdaLayersStack


app: core.App = core.App()
stack: LambdaLayersStack = LambdaLayersStack(
    app,
    "test",
    "test",
)
template: assertions.Template = assertions.Template.from_stack(stack)


def test_app_synthesize_ok():
    app.synth()
