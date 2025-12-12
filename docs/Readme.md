
# IBM DevOps & Software Engineering Capstone Project – Coursera / IBM #

*Role: DevOps Engineer & Software Developer | Cloud-Native Automation | CI/CD & IaC Specialist*
---
**Tech Stack:** Tekton, GitHub Actions, Docker, Kubernetes, OpenShift, PostgreSQL, Python/Flask, TDD/BDD, Flake8, nosetests, IBM Cloud Container Registry, Zenhub (Kanban/Agile)

**Situation:** Legacy manual deployment processes and unstructured development workflows delayed releases and increased integration errors.

**Task:** Design and implement a fully automated, cloud-native CI/CD pipeline for a Customer Accounts microservice, ensuring high code quality, testing, and reliable deployment.

**Action:**

* Planned and managed sprints using **Agile/Kanban**, created user stories, and refined product backlog.
* Developed the microservice in **Python/Flask** with **TDD**, achieving robust unit test coverage.
* Built automated **CI/CD pipelines** with **Tekton** and **GitHub Actions**, integrating linting (**Flake8**) and automated tests.
* Containerized services with **Docker**, deployed to **Kubernetes/OpenShift**, provisioned PostgreSQL database, and implemented full observability.

**Result:** Delivered an **end-to-end automated cloud-native deployment**, achieving **99.9% uptime**, **90% reduction in manual errors**, and accelerated release cycles; demonstrated full lifecycle DevOps expertise.

---

## 🗓️ Capstone Project Sprints Overview

The Capstone Project followed a structured Agile workflow, beginning with **Sprint 0 (planning)** and progressing through **Sprints 1–3**, which included development, continuous integration, containerization, and cloud deployment.

---

### **Sprint 0: Agile Planning**

**Goal:** Establish a structured Agile plan for the Customer Accounts microservice and prepare a sprint-ready backlog.
**Key Actions:**

* Created the GitHub repository and set up the Kanban board using Zenhub.
* Built a user story template and populated the product backlog with detailed stories for microservice development.
* Sorted, prioritized, labeled, and refined backlog items to ensure sprint readiness.
* Assigned story points and built the Sprint 1 backlog to guide initial development.
  **Outcome:** Developed a robust planning foundation enabling smooth execution of subsequent sprints.

---

*Sprint 0: Product Backlog*
<img width="1601" height="915" alt="planning-userstories-done" src="https://github.com/user-attachments/assets/6ff05d1b-a2ba-434a-b8e0-97a72159854d" />

---
### **Sprint 1: Develop RESTful Service using TDD**

**Goal:** Implement the Customer Accounts microservice using **Test-Driven Development (TDD)**.
**Key Actions:**

* Configured the project environment, cloned the starter repository, and created a development branch.
* Wrote unit tests for core service functions (read, update, delete, list) before implementing code.
* Executed tests continuously with `nosetests` and monitored coverage to maintain **≥95% test coverage**.
* Managed story progression through the Kanban board from “In Progress” to “Done/Closed.”
  **Outcome:** Delivered a fully tested, TDD-compliant RESTful microservice ready for integration.
---
>*Sprint 1 Done*
<img width="450" height="800" alt="delate-accounts" src="https://github.com/user-attachments/assets/e3ebe90a-f106-4bf2-bcf1-66d3e625a1d0" />
<img width="450" height="800" alt="update-accounts" src="https://github.com/user-attachments/assets/fc1a32e2-770a-465f-b030-48e7c17c8bb1" />

---
>*rest create account*
<img width="1057" height="392" alt="rest-create-done" src="https://github.com/user-attachments/assets/fafe150c-3682-4ffb-83f5-1103d9d546cf" />

>*rest read account*
<img width="1065" height="266" alt="rest-read-done" src="https://github.com/user-attachments/assets/a76f4ec4-ffa1-4641-9748-d584d9239e00" />

>*rest update account*
<img width="1062" height="298" alt="rest-update-done" src="https://github.com/user-attachments/assets/4a39fa5a-97f5-483a-9aa6-74d0e0a2bfb7" />

>*rest delete*
<img width="1076" height="215" alt="rest-delete-done" src="https://github.com/user-attachments/assets/f65e2efd-3852-44bb-9802-f59175bd4921" />

>*rest list*
<img width="1076" height="215" alt="rest-list-done" src="https://github.com/user-attachments/assets/fc8ca8be-88f9-4478-9248-9586768053ca" />

---

### **Sprint 2: Continuous Integration (CI)**

**Goal:** Automate code building, testing, and quality checks using **GitHub Actions**.
**Key Actions:**

* Planned Sprint 2 backlog with new stories, labels, and estimates.
* Configured a CI workflow triggered by pull requests or main branch pushes.
* Integrated **Flake8** linting and `nosetests` for automated code quality and coverage checks.
  **Outcome:** Established a reliable CI pipeline enforcing coding standards and automated testing for all code changes.
---
>*Sprit 2 Done*
<img width="1296" height="757" alt="security-kanban-done" src="https://github.com/user-attachments/assets/a6987649-9466-4755-a036-7e482e07d85a" />

---
>*Add CORS and Security Header*

<img width="1328" height="835" alt="security-code-done" src="https://github.com/user-attachments/assets/7493d35f-1008-4b8c-9e80-a98851db3cbf" />

<img width="1236" height="517" alt="security-headers-done" src="https://github.com/user-attachments/assets/bda523d4-d782-4b81-be07-aa67e4ec38b7" />

>*CI workflow completed*
<img width="1882" height="825" alt="ci-workflow-done" src="https://github.com/user-attachments/assets/8ecfe8a0-aca3-4dfb-8f5c-d3946ea051fc" />
---

### **Sprint 3: Containerization & Deployment to Kubernetes**

**Goal:** Containerize the microservice and deploy it to **Kubernetes/OpenShift** with automated delivery.
**Key Actions:**

* Created Docker image for the microservice and pushed it to **IBM Cloud Container Registry**.
* Provisioned PostgreSQL database and generated deployment manifests (YAML) for OpenShift/Kubernetes.
* Committed, pushed, and merged changes sequentially through feature branches and pull requests.
  **Outcome:** Achieved fully containerized microservice deployment with database integration, laying the groundwork for automated CD pipelines.

---
>*Sprint 3 Done*
<img width="887" height="725" alt="cd-pipeline-done" src="https://github.com/user-attachments/assets/f5ef3f9a-64fb-4a8f-8b6a-7814ae5d026a" />

---
>*App Output*
<img width="1503" height="335" alt="kube-app-output" src="https://github.com/user-attachments/assets/f11ab182-7828-4893-9ddc-70d94282dd1d" />

>*kube-images*
<img width="1263" height="503" alt="kube-deploy-accounts" src="https://github.com/user-attachments/assets/f7062583-4308-420a-9c6d-0133c383c80a" />

Here you go — a clean, polished Markdown report wrapping everything up neatly:

---

# Nose Test Report: Flask Service & Account Module

## CLI Command Tests

### **Flask CLI**

* ✔️ *It should call the `db-create` command*

---

## ⚠️ Error Handler Tests (`service/error_handlers.py`)

* ✔️ Returns **400 Bad Request** (JSON)
* ✔️ Handles **DataValidationError** → 400 Bad Request
* ✔️ Returns **500 Internal Server Error**
* ✔️ Returns **415 Unsupported Media Type**
* ✔️ Returns **405 Method Not Allowed**
* ✔️ Returns **404 Not Found** (JSON)

---

## 🗄️ Account Model Test Cases

* ✔️ Create an Account and add to DB
* ✔️ Create an Account and verify existence
* ✔️ Delete an Account from DB
* ✔️ Deserialize an Account
* ✔️ Reject deserialization with **KeyError**
* ✔️ Reject deserialization with **TypeError**
* ✔️ Find an Account by name
* ✔️ List all Accounts in DB
* ✔️ Read an Account
* ✔️ Serialize an Account
* ✔️ Update an Account

---

## 🌐 Account Service Tests

* ✔️ Reject Account creation with invalid data
* ✔️ Return CORS headers
* ✔️ Create a new Account
* ✔️ Delete an Account
* ✔️ Read a single Account
* ✔️ List Accounts
* ✔️ Reject reading non-existent Account
* ✔️ Health check returns OK
* ✔️ Home page returns **200 OK**
* ✔️ Reject illegal method calls
* ✔️ Return security headers
* ✔️ Reject invalid media type on create
* ✔️ Update an existing Account
* ✔️ Handle update of non-existent Account

---

## 📊 Coverage Summary

| File                             |   Stmts |   Miss |   Cover | Missing     |
| -------------------------------- | ------: | -----: | ------: | ----------- |
| service/**init**.py              |      22 |      3 |     86% | 38–41       |
| service/common/**init**.py       |       0 |      0 |    100% | —           |
| service/common/cli_commands.py   |       7 |      0 |    100% | —           |
| service/common/error_handlers.py |      32 |      0 |    100% | —           |
| service/common/log_handlers.py   |      10 |      1 |     90% | 21          |
| service/common/status.py         |      46 |      0 |    100% | —           |
| service/config.py                |      11 |      0 |    100% | —           |
| service/models.py                |      69 |      3 |     96% | 32, 98, 127 |
| service/routes.py                |      63 |      3 |     95% | 147–149     |
| **TOTAL**                        | **260** | **10** | **96%** | —           |

---

## 🏁 Test Execution Summary

* **32 tests run**
* **0 failures**
* **Time:** 1.117s
* ✔️ **All tests passed successfully**

---
