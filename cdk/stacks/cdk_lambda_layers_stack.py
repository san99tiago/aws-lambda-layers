# Built-in imports
import os

# External imports
from aws_cdk import (
    Stack,
    Duration,
    CfnOutput,
    aws_lambda,
    RemovalPolicy,
)
from constructs import Construct


class LambdaLayersStack(Stack):
    """
    Class to create the infrastructure on AWS.
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        main_resources_name: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Input parameters
        self.construct_id = construct_id
        self.main_resources_name = main_resources_name

        # Main methods for the deployment
        self.create_lambda_layers()

        # Create CloudFormation outputs
        self.generate_cloudformation_outputs()

    def create_lambda_layers(self):
        """
        Create the Lambda layers that are necessary for the additional runtime
        dependencies of the Lambda Functions.
        """

        # Layer for "yfinance" Python3.12 libraries
        self.lambda_layer_yfinance_py_3_12 = aws_lambda.LayerVersion(
            self,
            "LambdaLayer-yfinance-3-12",
            layer_version_name="python3-12-yfinance",
            description="Lambda Layer for Python3.12 with <yfinance> library",
            code=aws_lambda.Code.from_asset("lambda-layers/yfinance/modules"),
            compatible_runtimes=[
                aws_lambda.Runtime.PYTHON_3_12,
            ],
            compatible_architectures=[aws_lambda.Architecture.X86_64],
            license="Apache",
            removal_policy=RemovalPolicy.RETAIN,
        )

        self.lambda_layer_yfinance_py_3_12.add_permission(
            "LambdaLayer-yfinance-3-12-permissions",
            account_id="*",
        )

    def generate_cloudformation_outputs(self):
        """
        Method to add the relevant CloudFormation outputs.
        """

        CfnOutput(
            self,
            "YFINANCELambdaLayerLatestArn",
            value=self.lambda_layer_yfinance_py_3_12.layer_version_arn,
            description="Yfinance Lambda Layer ARN",
        )
