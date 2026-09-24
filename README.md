# CC-Experiment-01: Performance Analysis of Type-1 and Type-2 Hypervisors

## 1. Experiment Title

**Performance Analysis of Type-1 and Type-2 Hypervisors**

## 2. Aim

To create and configure identically resourced Ubuntu virtual machines on a **Type-1 hypervisor (Proxmox VE)** and a **Type-2 hypervisor (VMware Workstation)** and compare their CPU performance using the **Sysbench CPU benchmark**.

## 3. Objectives

The objectives of this experiment are:

* To understand the concept of virtualization and the role of hypervisors.
* To study the differences between Type-1 and Type-2 hypervisors.
* To configure and run an Ubuntu virtual machine on **Proxmox VE**.
* To configure and run an Ubuntu virtual machine on **VMware Workstation**.
* To allocate identical CPU, memory, and other relevant resources to both virtual machines.
* To perform CPU benchmarking using **Sysbench**.
* To collect CPU performance metrics from both virtualization environments.
* To compare **execution time, total events, events per second, and average latency**.
* To analyze the effect of the virtualization layer on CPU performance.
* To document the experimental procedure, observations, screenshots, and benchmark results.

## 4. Introduction

### 4.1 Virtualization

Virtualization is a technology that enables physical computing resources such as **CPU, memory, storage, and network interfaces** to be abstracted and allocated to multiple virtual machines.

A **Virtual Machine (VM)** is a software-based computer system that operates independently within a physical computer. It has its own virtual CPU, memory, storage, network interface, and operating system.

Virtualization allows multiple virtual machines to run simultaneously on the same physical hardware while maintaining a degree of isolation between them.

### 4.2 Hypervisor

A **hypervisor**, also known as a **Virtual Machine Monitor (VMM)**, is the software or virtualization layer responsible for creating, running, and managing virtual machines.

The hypervisor manages the allocation of physical hardware resources to virtual machines and provides isolation between different guest operating systems.

Hypervisors are commonly classified into two categories:

1. **Type-1 Hypervisor**
2. **Type-2 Hypervisor**

## 5. Types of Hypervisors

### 5.1 Type-1 Hypervisor

A **Type-1 hypervisor**, also called a **bare-metal hypervisor**, runs directly on the physical hardware.

It does not depend on a conventional desktop host operating system for its primary virtualization functions. The hypervisor manages the physical hardware and provides resources to the virtual machines.

In this experiment, **Proxmox VE** is used as the Type-1 virtualization platform.

### Architecture

```text
┌────────────────────────────────────┐
│          Virtual Machines          │
│                                    │
│   ┌─────────┐    ┌─────────┐      │
│   │   VM 1  │    │   VM 2  │ ...  │
│   └─────────┘    └─────────┘      │
├────────────────────────────────────┤
│          Type-1 Hypervisor         │
│             Proxmox VE             │
├────────────────────────────────────┤
│          Physical Hardware         │
│        CPU / RAM / Storage         │
└────────────────────────────────────┘
```

**Examples of Type-1 hypervisors:** Proxmox VE, VMware ESXi, Microsoft Hyper-V, and Xen.

### 5.2 Type-2 Hypervisor

A **Type-2 hypervisor**, also known as a **hosted hypervisor**, runs as an application on top of a conventional host operating system.

The host operating system manages the physical hardware, while the Type-2 hypervisor provides the environment required to create and run virtual machines.

In this experiment, **VMware Workstation** is used as the Type-2 virtualization platform.

### Architecture

```text
┌────────────────────────────────────┐
│          Virtual Machines          │
│                                    │
│   ┌─────────┐    ┌─────────┐      │
│   │   VM 1  │    │   VM 2  │ ...  │
│   └─────────┘    └─────────┘      │
├────────────────────────────────────┤
│          Type-2 Hypervisor         │
│        VMware Workstation          │
├────────────────────────────────────┤
│        Host Operating System       │
│        Windows / Linux / etc.      │
├────────────────────────────────────┤
│          Physical Hardware         │
│        CPU / RAM / Storage         │
└────────────────────────────────────┘
```

**Examples of Type-2 hypervisors:** VMware Workstation, Oracle VirtualBox, and Parallels Desktop.

## 6. Comparison of Type-1 and Type-2 Hypervisors

| Feature         | Type-1 Hypervisor                    | Type-2 Hypervisor                        |
| --------------- | ------------------------------------ | ---------------------------------------- |
| Installation    | Directly on physical hardware        | On top of a host OS                      |
| Host OS         | Not required for primary operation   | Required                                 |
| Example         | Proxmox VE                           | VMware Workstation                       |
| Hardware access | More direct                          | Through host OS and virtualization layer |
| Typical usage   | Servers, data centers, labs          | Desktop, development, testing            |
| Management      | Dedicated virtualization environment | Managed through host OS                  |
| Overhead        | Generally lower                      | Generally higher due to host OS layer    |

## 7. Experimental Concept

For a fair comparison, the Ubuntu virtual machines should be configured with the same or equivalent resources in both environments.

The following parameters should be kept identical wherever possible:

* Guest operating system: **Ubuntu**
* Number of virtual CPUs: **Same for both VMs**
* Allocated RAM: **Same for both VMs**
* Disk configuration: **Equivalent**
* Sysbench test parameters: **Same**
* Number of CPU benchmark threads: **Same**
* Benchmark duration/workload: **Same**

The Sysbench CPU benchmark is then executed inside both Ubuntu virtual machines. The resulting metrics are recorded and compared.

Important metrics include:

* **Total execution time**
* **Total number of events**
* **Events per second**
* **Average latency**
* **Maximum latency**, if reported

The experiment helps demonstrate how the virtualization architecture and execution environment can affect the performance observed by a guest operating system.

## 8. Expected Outcome

The experiment is expected to produce measurable differences in CPU benchmark results between the Ubuntu VM running on Proxmox VE and the Ubuntu VM running on VMware Workstation.

The results should be analyzed using the actual measurements obtained during the experiment rather than assuming that one virtualization platform will always provide better performance.

## 9. Result

The CPU performance of identically configured Ubuntu virtual machines running on a **Type-1 hypervisor (Proxmox VE)** and a **Type-2 hypervisor (VMware Workstation)** will be measured using Sysbench.

The measured values for execution time, total events, events per second, and latency will be recorded and compared to determine the observed performance difference between the two virtualization environments.
