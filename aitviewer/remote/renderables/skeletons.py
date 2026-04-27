# Copyright (C) 2023  ETH Zurich, Manuel Kaufmann, Velko Vechev, Dario Mylonopoulos
from ..message import Message
from ..node import RemoteNode


class RemoteSkeletons(RemoteNode):
    MESSAGE_TYPE = Message.SKELETONS

    def __init__(self, viewer, joint_positions, joint_connections, **kwargs):
        """
        This initializer takes a RemoteViewer object and all other arguments are forwarded
        to the Spheres constructor on the remote Viewer.
        See the Spheres class for more information about parameters.

        :param viewer: a RemoteViewer object that will be used to send this node.
        :param joint_positions: A np array of shape (F, J, 3) containing J joint positions over F many time steps.
        :param joint_connections: The definition of the skeleton as a numpy array of shape (N_LINES, 2) where each row
          defines one connection between joints. The max entry in this array must be < J.
        """
        super().__init__(
            viewer,
            joint_positions=joint_positions,
            joint_connections=joint_connections,
            **kwargs,
        )

    def add_frames(self, joint_positions):
        """
        Add frames to the remote Spheres node by adding new sphere positions.

        :param joint_positions: A np array of shape (N, J, 3) or (J, 3) containing J joint positions.
        """
        return super().add_frames(joint_positions=joint_positions)

    def update_frames(self, joint_positions, frames):
        """
        Update frames of the remote Spheres node by updating the sphere positions.

        :param joint_positions: A np array of shape (N, J, 3) containing J joint positions.
        :param frames: a list of integer frame indices of size N or a single integer frame index.
        """
        return super().update_frames(joint_positions=joint_positions, frames=frames)
