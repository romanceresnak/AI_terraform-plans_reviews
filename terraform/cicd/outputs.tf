output "repository_clone_url_http" {
  description = "The HTTP clone URL for the CodeCommit repository"
  value       = aws_codecommit_repository.repo.clone_url_http
}

output "pipeline_url" {
  description = "The URL to the CodePipeline"
  value       = "https://${var.aws_region}.console.aws.amazon.com/codesuite/codepipeline/pipelines/${aws_codepipeline.pipeline.name}/view?region=${var.aws_region}"
}
