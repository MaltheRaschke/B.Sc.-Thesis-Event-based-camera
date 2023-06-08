# B.Sc.-Thesis-Event-based-camera
B.Sc.-thesis repository contains Python code, ROS packages, trained models, generated train/ test datasets and inference results.
!! Not all bagfiles for the raw test-data are included as they are too big for GitHub (the RetinaNet neural network .pt files was also too big) !!

- After installing Unreal Engine 4.27 and AirSim from https://microsoft.github.io/AirSim/ the event_pack package should be placed in catkin_ws.
- The "datagen" package is available from https://github.com/phxhuy/datagen for generating flying scenarios.
- The "dv-ros" package for the iniVation DVXplorer mini event-based camera is available from https://gitlab.com/inivation/dv/dv-ros

Video clips are available in the inference results for review of the predicted bboxes.
All labelled training data and test data ground truth is available at: https://app.roboflow.com/au-bachelor-projekt-kqx8k
