resource "aws_s3_bucket" "example" {
  bucket = "my-ai-reviewed-bucket-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name        = "AI Reviewed Bucket"
    Environment = "Production"
    Project     = "Terraform AI Review Demo"
    ManagedBy   = "Terraform"
    Owner       = "DevOps Team"
  }
}

resource "aws_s3_bucket_versioning" "example" {
  bucket = aws_s3_bucket.example.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "example" {
  bucket = aws_s3_bucket.example.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.example.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_logging" "example" {
  bucket = aws_s3_bucket.example.id

  target_bucket = aws_s3_bucket.logs.id
  target_prefix = "access-logs/"
}

resource "aws_s3_bucket" "logs" {
  bucket = "my-ai-reviewed-bucket-logs-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name        = "AI Reviewed Bucket Logs"
    Environment = "Production"
    Project     = "Terraform AI Review Demo"
    ManagedBy   = "Terraform"
    Owner       = "DevOps Team"
  }
}

resource "aws_s3_bucket_public_access_block" "logs" {
  bucket = aws_s3_bucket.logs.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

data "aws_caller_identity" "current" {}
