import threading
import time
from datetime import datetime

import numpy as np

from reachy_mini import ReachyMini, ReachyMiniApp
from reachy_mini.utils import create_head_pose


class TeamGreetingApp(ReachyMiniApp):
    """A simple three-stage greeting behavior for Reachy Mini."""

    custom_app_url: str | None = None
    request_media_backend: str | None = None

    # Named motion/timing parameters
    ORIENT_YAW_DEG = 20.0          # degrees
    ANTENNA_AMPLITUDE_DEG = 20.0   # degrees
    ORIENT_DURATION_SEC = 2.0      # seconds
    GREETING_DURATION_SEC = 3.0    # seconds
    CONTROL_PERIOD_SEC = 0.05      # seconds

    def log_stage(self, message: str):
        """Print a timestamped stage marker."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}", flush=True)

    def wait_with_stop(self, duration: float, stop_event: threading.Event):
        """Wait while checking for a stop request."""
        end_time = time.time() + duration
        while time.time() < end_time:
            if stop_event.is_set():
                return False
            time.sleep(self.CONTROL_PERIOD_SEC)
        return True

    def return_to_neutral(self, reachy_mini: ReachyMini):
        """Return head and antennas to a neutral pose."""
        neutral_head = create_head_pose(yaw=0.0, degrees=True)
        neutral_antennas = np.deg2rad(np.array([0.0, 0.0]))

        reachy_mini.set_target(
            head=neutral_head,
            antennas=neutral_antennas,
        )

    def run(self, reachy_mini: ReachyMini, stop_event: threading.Event):
        try:
            # Stage 1: orient toward the implied user
            self.log_stage("STAGE 1 - ORIENT")

            orient_head = create_head_pose(
                yaw=self.ORIENT_YAW_DEG,
                degrees=True,
            )

            reachy_mini.set_target(
                head=orient_head,
                antennas=np.deg2rad(np.array([0.0, 0.0])),
            )

            if not self.wait_with_stop(self.ORIENT_DURATION_SEC, stop_event):
                return

            # Stage 2: greeting using head + antennas
            self.log_stage("STAGE 2 - GREETING")
            start_time = time.time()

            while (
                time.time() - start_time < self.GREETING_DURATION_SEC
                and not stop_event.is_set()
            ):
                t = time.time() - start_time

                antenna_angle = (
                    self.ANTENNA_AMPLITUDE_DEG
                    * np.sin(2.0 * np.pi * 1.0 * t)
                )
                antennas = np.deg2rad(
                    np.array([antenna_angle, -antenna_angle])
                )

                greeting_yaw = 8.0 * np.sin(2.0 * np.pi * 0.5 * t)
                greeting_head = create_head_pose(
                    yaw=greeting_yaw,
                    degrees=True,
                )

                reachy_mini.set_target(
                    head=greeting_head,
                    antennas=antennas,
                )

                time.sleep(self.CONTROL_PERIOD_SEC)

            # Stage 3: return to neutral
            self.log_stage("STAGE 3 - RETURN TO NEUTRAL")
            self.return_to_neutral(reachy_mini)

            if not self.wait_with_stop(1.0, stop_event):
                return

            self.log_stage("GREETING COMPLETE")

        finally:
            # Always leave the robot in a neutral pose.
            self.return_to_neutral(reachy_mini)

            if stop_event.is_set():
                self.log_stage("STOP REQUESTED - RETURNED TO NEUTRAL")


if __name__ == "__main__":
    app = TeamGreetingApp()

    try:
        app.wrapped_run()
    except KeyboardInterrupt:
        app.stop()
