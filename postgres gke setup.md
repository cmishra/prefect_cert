# Setting up a GKE cluster for a new environment
There's a few steps here:

Create a new cluster https://console.cloud.google.com/kubernetes/list/overview. Try to give it the name autopilot-cluster-1 otherwise you have to change the commands here. 

Create a k8s service account

```
kubectl create serviceaccount --namespace default gke-service-account
```
If you don't already have a GCP service account you want to use, then create one:
```
gcloud iam service-accounts create gke-service-account \
   --project=chetanmishra
gcloud projects add-iam-policy-binding example-project-id \
   --member "serviceAccount:gke-service-account@chetanmishra.iam.gserviceaccount.com" \
   --role "editor"
```
Connect the GCP service account and the kubernetes service account:
```
gcloud iam service-accounts add-iam-policy-binding gke-service-account@chetanmishra.iam.gserviceaccount.com \
   --role roles/iam.workloadIdentityUser \
   --member "serviceAccount:chetanmishra.svc.id.goog[default/gke-service-account]" \
   --project chetanmishra
```
Run this last command that does something
```
kubectl annotate serviceaccount gke-service-account \
   --namespace default \
   iam.gke.io/gcp-service-account=gke-service-account@chetanmishra.iam.gserviceaccount.com
```
Deploy your workloads.
