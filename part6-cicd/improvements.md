Part 6: CI/CD PIPELINE REVIEW (15 minutes)
Tasks:
  Q1. Identify problems with this pipeline (minimum 4)
     1.	No build stage separation
     2. No security scanning
     3. No approval step
     4. Direct deploy to prod
     5. No environment separation

    
  Q2. Propose improvements for a production-ready CI/CD pipeline including:
     - Security scanning
        1. SAST (Bandit)
        2. Dependency scan (Snyk)

     - Testing strategy
        1. Unit + Integration tests
        2. Coverage check

     - Approval gates
        1. Build → Test → Security Scan → Staging → Approval → Production

     - Rollback mechanism
        1. Blue/Green deployment
        2. Keep previous version artifacts

     - Environment promotion (dev staging  prod)