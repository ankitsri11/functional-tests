// --GO-LICENSE-START--
// Copyright 2015 ThoughtWorks, Inc.
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//    http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// --GO-LICENSE-END--

KillProcessTreeWhenStageCancel
==============================

Setup of contexts
* Basic configuration - setup
* Using pipeline "process-tree" - setup
* With "1" live agents in directory "kill_process_tree" - setup
* Capture go state "KillProcessTreeWhenStageCancel" - setup

KillProcessTreeWhenStageCancel
------------------------------

tags: 3544, automate, cancel, kill-process

* Commit file "fork_self.rake"

* Looking at pipeline "process-tree"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1"

* Navigate to job "defaultJob"

* Wait for log "Current counter 1"

* On Pipeline Dashboard Page
* Looking at pipeline "process-tree"
* Navigate to stage "defaultStage" of run "1"

* Cancel "defaultStage" - Already On Stage Detail Page

* On Agents Page
* Wait for agent to show status "idle"

* On Pipeline Dashboard Page
* Looking at pipeline "process-tree"
* Navigate to stage "defaultStage" of run "1"

* Navigate to job "defaultJob"

* Open console tab
* Verify console contains "Current counter 10"
* Verify console contains "Current counter 2"
* Verify console contains "Current counter 1"
* Verify console does not contain "Process was not killed, it returned."




Teardown of contexts
____________________
* Capture go state "KillProcessTreeWhenStageCancel" - teardown
* With "1" live agents in directory "kill_process_tree" - teardown
* Using pipeline "process-tree" - teardown
* Basic configuration - teardown


