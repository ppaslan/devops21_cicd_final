# Intro

This is a simple containerized application running on Kubernetes, Argocd continuously monitors this repo, pulling any recent changes and updating the state of the application in Kubernetes.
This project uses helm charts for easy application and package management.


# Installation

## Kubernetes and argocd

1. [Install Rancher Desktop](https://docs.rancherdesktop.io/getting-started/installation)
2. Clone this repo
3. `kubectl apply -f argocd/install.yaml`
4. `kubectl apply -f argocd/argocd-shop-instances.yaml`

## Application instance

1.  `./create_secrets.sh -n shop-production -s ghcr.io -u github-username -t github-token -e email`
2. `cp -r template/shopapp-template instances/shop-production`
3. `cp template/shopapp-template.yaml instances/shop-production.yaml`
4. Edit `instances/kustomization.yaml` and make it look like this
    ```yaml
    ---
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    metadata:
    name: shop-instances

    resources:
    - shop-production.yaml

    ```
5. Edit `instances/shop-production.yaml` and make it look like this.
    ```yaml
    ---
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
    name: shop-production
    namespace: argocd
    spec:
    project: default
    source:
        repoURL: git@github.com:ppaslan/devops21_cicd_final
        targetRevision: main
        path: instances/shop-production
    destination:
        server: https://kubernetes.default.svc
        namespace: shop-production
    syncPolicy:
        automated: {}
        syncOptions:
        - CreateNamespace=true
    ```

Argocd is now setup to monitor your instances/ folder for new application and deploy them to the cluster.
If Argocd notices any changes in the helm charts then it will make sure to update the state of your application in kubernetes.

## Environment

Follow the README.md in src/ folder
