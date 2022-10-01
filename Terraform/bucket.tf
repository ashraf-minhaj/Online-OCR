# create a bucket notification for lambda to be invoked by
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = "${var.input_bucket_name}"

  lambda_function {
    lambda_function_arn = "${aws_lambda_function.lambda.arn}"
    events              = ["s3:ObjectCreated:*"]
  }
}