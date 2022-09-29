# Zip the Lamda function on the fly
data "archive_file" "source" {
  type        = var.lambda_archive_file_type
  source_dir  = var.lambda_source_path
  output_path = var.lambda_zip_output_path
}

# upload zip to s3 and then update lamda function from s3
resource "aws_s3_object" "s3_bucket_obj" {
  bucket = var.lambda_bucket
  key    = var.lambda_bucket_key
  source = data.archive_file.source.output_path
}


# connect this lambda with uploaded s3 zip file
# lambda needs code and iam_role
# "${aws_s3_bucket_object.file_upload.key}"
# resource - resource_name

# create a lambda function
resource "aws_lambda_function" "lambda" {
    function_name   = "${var.component_prefix}-${var.component_name}"
    architectures = [ "arm64" ]
    s3_bucket       = aws_s3_object.s3_bucket_obj.bucket
    s3_key          = aws_s3_object.s3_bucket_obj.key
    role            = aws_iam_role.lambda_role.arn 
    handler         = "${var.component_prefix}-${var.component_name}.${var.lambda_handler}"
    runtime         = var.lambda_runtime
    timeout         = var.lambda_timeout
}


# add invoke permission
resource "aws_lambda_permission" "lambdaInvokePermission" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.arn
  principal     = "s3.amazonaws.com"
  source_arn    = "arn:aws:s3:::${var.input_bucket_name}"
}

# arn:aws:s3:::bucket