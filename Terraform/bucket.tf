# create a bucket notification for lambda to be invoked by
resource "aws_s3_bucket" "s3" {
    bucket = "${var.bucket_name}"   
    # policy = data.aws_iam_policy_document.website_policy.json
    # website {
    #   index_document = "src/index.html"
    #   error_document = "src/index.html"
    #   }
}

# making the s3 bucket private 
resource "aws_s3_bucket_acl" "s3_bucket_acl" {
  bucket = aws_s3_bucket.s3.id
  acl    = "private"
}

resource "aws_s3_bucket_object" "objects" {
for_each = fileset("../src/", "*")
bucket = aws_s3_bucket.s3.id
key = each.value
source = "../src/${each.value}"
etag = filemd5("src/${each.value}")
}