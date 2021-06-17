#Finds the folder aws and gets the credentials
provider "aws" {
    profile = "default"
    region = "us-east-2"
}

#creating the s3 bucket
resource "aws_s3_bucket" "tf_course" {
    bucket="abdullahnaeem1"
    acl="private"
} 
