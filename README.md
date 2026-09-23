CC-Experiment-01: Performance Analysis of Type-1 and Type-2 Hypervisors
1. Experiment Title
Performance Analysis of Type-1 and Type-2 Hypervisors

2. Aim
To create identically configured virtual machines on a Type-1 hypervisor and a Type-2 hypervisor and compare their CPU performance using the Sysbench CPU benchmark.

3. Objectives
The objectives of this experiment are:

To understand virtualization and the role of hypervisors.
To understand the difference between Type-1 and Type-2 hypervisors.
To configure and run an Ubuntu virtual machine on Proxmox VE.
To configure and run an Ubuntu virtual machine on VMware Workstation.
To maintain identical VM resources for a fair comparison.
To perform CPU benchmarking using Sysbench.
To collect CPU performance metrics from both environments.
To compare execution time, total events, events per second, and latency.
To observe the effect of the virtualization environment on the measured CPU performance.
To document the complete experiment using screenshots and result files.
4. Introduction
4.1 Virtualization
Virtualization is a technology that allows physical computing resources such as CPU, memory, storage, and networking to be abstracted and allocated to virtual machines.

A virtual machine behaves like an independent computer with its own operating system, virtual CPU, memory, disk, and network interface.

Multiple virtual machines can therefore run on the same physical hardware.

4.2 Hypervisor
A hypervisor, also called a Virtual Machine Monitor (VMM), is the software layer responsible for creating and managing virtual machines.

It allocates physical hardware resources to virtual machines and provides isolation between different guest operating systems.

Hypervisors are broadly classified into two types:

Type-1 Hypervisor
Type-2 Hypervisor
5. Types of Hypervisors
5.1 Type-1 Hypervisor
A Type-1 hypervisor runs directly on the physical hardware.

There is no conventional host operating system between the physical hardware and the hypervisor.

Architecture
┌───────────────────────────────┐
│       Virtual Machines        │
│     ┌───────┐   ┌───────┐     │
│     │  VM 1 │   │  VM 2 │ ... │
│     └───────┘   └───────┘     │
├───────────────────────────────┤
│       Type-1 Hypervisor       │
│         Proxmox VE            │
├───────────────────────────────┤

## 5.2 Type-2 Hypervisor

A Type-2 hypervisor runs as an application on top of a host operating system.

The host operating system manages the physical hardware, while the hypervisor provides the virtualization environment for running guest virtual machines.

### Architecture

┌───────────────────────────────┐
│       Virtual Machines        │
│     ┌───────┐   ┌───────┐     │
│     │  VM 1 │   │  VM 2 │ ... │
│     └───────┘   └───────┘     │
├───────────────────────────────┤
│       Type-2 Hypervisor       │
│     VMware Workstation        │
├───────────────────────────────┤
│      Host Operating System    │
├───────────────────────────────┤
│       Physical Hardware       │
│       CPU / RAM / Disk        │
└───────────────────────────────┘
│       Physical Hardware       │
│       CPU / RAM / Disk        │
└───────────────────────────────┘
