variable "aws_region" {
	default = "ap-south-1"
}

variable "aws_access_key" {
  default = ""
}

variable "aws_secret_key" {
  default = ""
}

variable "region" {
  
}


# store the zip file here
variable "input_bucket_name" {
	
}

variable "component_prefix" {
  default = "img2txt"
}

variable "component_name" {
  default = "textextractor"
}

variable "lambda_bucket" {
  default     = ""
  description = "store lambda in this bucket"
}

variable "lambda_bucket_key" {
  default     = "lambda/img2txt-textextractor.zip"
  description = "Store zip file in this bucket path"
}

variable "lambda_source_path" {
  default = "../src/"
}

variable "lambda_zip_output_path" {
  default = "../output_files/--.zip"
}

variable "lambda_archive_file_type" {
  default = "zip"
}


variable "lambda_handler" {
  default = "handler"
}

variable "lambda_runtime" {
  default = "python3.9"
}

# variable "lambda_architecture" {
#   default = "arm64"
# }

variable "lambda_timeout" {
  default = "10"
}