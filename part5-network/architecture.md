Here’s a clean, practical design you can present for TechKraft’s redundant DNS architecture using AWS Route 53, tailored for Nepal/South Asia.

⸻

🧩 1. Architecture Overview (ASCII Diagram)

                    ┌──────────────────────────────┐
                    │        Route 53 (DNS)        │
                    │  Public Hosted Zone          │
                    └────────────┬─────────────────┘
                                 │
                ┌────────────────┴────────────────┐
                │                                 │
     ┌──────────▼──────────┐           ┌──────────▼──────────┐
     │ Primary Endpoint    │           │ Secondary Endpoint  │
     │ (Active)            │           │ (Failover)          │
     │ ALB (ap-south-1)    │           │ ALB (ap-south-1 or  │
     │ Mumbai Region       │           │ ap-southeast-1)     │
     └──────────┬──────────┘           └──────────┬──────────┘
                │                                 │
        ┌───────▼────────┐                ┌──────▼────────┐
        │ EC2 + Unbound  │                │ EC2 + Unbound │
        │ DNS Servers    │                │ DNS Servers   │
        │ (Multi-AZ)     │                │ (Multi-AZ)    │
        └────────────────┘                └───────────────┘
                ↑
        Route 53 Health Checks



 2. Key Components & Purpose

1. Amazon Route 53

* Acts as the global DNS entry point
* Handles failover routing + health checks
* Highly available by default (no need to manage infra)



2. Primary Endpoint (Active)

* Region: Mumbai (ap-south-1) → closest to Nepal
* Components:
    * Application Load Balancer (ALB)
    * EC2 instances running Unbound DNS
* Multi-AZ deployment → internal redundancy



3. Secondary Endpoint (Failover)

* Region options:
    * Same region (ap-south-1) for cost efficiency
    * OR Singapore (ap-southeast-1) for disaster resilience
* Mirrors primary stack



4. Health Checks

* Configured in Route 53
* Checks:
    * DNS port (53)
    * OR HTTP endpoint like /health
* Interval: 30s (or 10s for faster failover)



3. Failover Logic

Using Route 53 Failover Routing Policy:

* Primary record (A/AAAA)
    * Points to primary ALB
    * Has health check attached
* Secondary record
    * Marked as failover = secondary
    * Activated only when primary fails

Flow:

1. Route 53 sends traffic → Primary
2. Health check fails ❌
3. Route 53 automatically routes → Secondary
4. Recovery → traffic shifts back



4. Latency Considerations (Nepal / South Asia)

* Nepal users get best latency from:
    * Mumbai (ap-south-1) ← primary choice
* Singapore fallback gives:
    * Slightly higher latency but better regional resilience

Optimization:

* Use:
    * Latency-based routing (optional) + failover
* Enable:
    * Route 53 health checks + latency routing hybrid
 5. Cost Estimate (Monthly – Rough)

Component	Cost (USD/month)
Route 53 Hosted Zone	~$0.50
DNS Queries (~1M)	~$0.40
Health Checks (2–4)	~$2–4
ALB (2 regions)	~$20–40
EC2 (t3.micro x4)	~$20–30
Data Transfer	~$5–10
 Total Estimate:  $50 – $85 / month

Cost Optimization Tips:

* Use t3.micro / t4g.micro
* Keep secondary in same region (if DR not critical)
* Reduce health check frequency (30s instead of 10s)



6. Implementation Timeline

Phase	Task	Time
Phase 1	Setup Route 53 hosted zone	1 hour
Phase 2	Deploy primary stack (ALB + EC2 + Unbound)	3–4 hours
Phase 3	Deploy secondary stack	2–3 hours
Phase 4	Configure health checks + failover routing	1–2 hours
Phase 5	Testing (failover simulation)	2 hours

 Total:   1–2 days



Final Design Summary

* Highly available DNS using Route 53
* Primary + Secondary failover
* Optimized for Nepal via Mumbai region
* Health-check-driven automatic recovery
* Cost-efficient (~$50/month baseline)

