from scripts.network import Network

import tensorflow as tf


class UNetResidual_Ext2(Network):

    def getOutput(self):
        return self.layers['conv9_2']

    def setup(self, is_training, num_classes):

        (self.feed('data')
                .conv(7, 7, 64, 1, 1, padding='SAME', relu=False, biased=True, name='conv1_1')
                .batch_normalization(relu=False, name='conv1_bn1')
                .dropout(keep_prob=0.9, is_training=is_training, name='conv1_dr1')
                .relu(name='conv1_rl1')
                .max_pool(2, 2, 2, 2, padding='VALID', name='conv1_mp1'))

        (self.feed('conv1_rl1')
                .residual_block(use_dropout=True, name='conv1_add_residual1')
                .residual_block(use_dropout=True, name='conv1_add_residual2')
                .residual_block(use_dropout=True, name='conv1_add_residual3')
                .residual_block(use_dropout=True, name='conv1_add_residual4')
                .residual_block(use_dropout=True, name='conv1_add_residual5')
                .residual_block(use_dropout=True, name='conv1_add_residual6')
                .residual_block(use_dropout=True, name='conv1_add_residual7')
                .residual_block(use_dropout=True, name='conv1_add_residual8')
                )

        (self.feed('conv1_mp1')
                .conv(3, 3, 128, 1, 1, padding='SAME', relu=False, biased=True, name='conv2_1')
                .batch_normalization(relu=False, name='conv2_bn1')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv2_dr1')
                .relu(name='conv2_rl1')
                .residual_block(use_dropout=True, name='conv2_residual1')
                .residual_block(use_dropout=True, name='conv2_residual2')
                .residual_block(use_dropout=True, name='conv2_residual3')
                .batch_normalization(relu=False, name='conv2_bn2')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv2_dr2')
                .relu(name='conv2_rl2')
                .max_pool(2, 2, 2, 2, padding='VALID', name='conv2_mp1'))

        (self.feed('conv2_rl2')
                .residual_block(use_dropout=True, name='conv2_add_residual1')
                .residual_block(use_dropout=True, name='conv2_add_residual2')
                .residual_block(use_dropout=True, name='conv2_add_residual3')
                .residual_block(use_dropout=True, name='conv2_add_residual4')
                .residual_block(use_dropout=True, name='conv2_add_residual5')
                .residual_block(use_dropout=True, name='conv2_add_residual6')
                )

        (self.feed('conv2_mp1')
                .conv(3, 3, 256, 1, 1, padding='SAME', relu=False, biased=True, name='conv3_1')
                .batch_normalization(relu=False, name='conv3_bn1')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv3_dr1')
                .relu(name='conv3_rl1')
                .residual_block(use_dropout=True, name='conv3_residual1')
                .residual_block(use_dropout=True, name='conv3_residual2')
                .residual_block(use_dropout=True, name='conv3_residual3')
                .residual_block(use_dropout=True, name='conv3_residual4')
                .batch_normalization(relu=False, name='conv3_bn2')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv3_dr2')
                .relu(name='conv3_rl2')
                .max_pool(2, 2, 2, 2, padding='VALID', name='conv3_mp1'))

        (self.feed('conv3_rl2')
                .residual_block(use_dropout=True, name='conv3_add_residual1')
                .residual_block(use_dropout=True, name='conv3_add_residual2')
                .residual_block(use_dropout=True, name='conv3_add_residual3')
                )

        (self.feed('conv3_mp1')
                .conv(3, 3, 512, 1, 1, padding='SAME', relu=False, biased=True, name='conv4_1')
                .batch_normalization(relu=False, name='conv4_bn1')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv4_dr1')
                .relu(name='conv4_rl1')
                .residual_block(use_dropout=True, name='conv4_residual1')
                .residual_block(use_dropout=True, name='conv4_residual2')
                .residual_block(use_dropout=True, name='conv4_residual3')
                .residual_block(use_dropout=True, name='conv4_residual4')
                .residual_block(use_dropout=True, name='conv4_residual5')
                .residual_block(use_dropout=True, name='conv4_residual6')
                .batch_normalization(relu=False, name='conv4_bn2')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv4_dr2')
                .relu(name='conv4_rl2')
                .max_pool(2, 2, 2, 2, padding='VALID', name='conv4_mp1'))

        (self.feed('conv4_mp1')
                .conv(3, 3, 512, 1, 1, padding='SAME', relu=False, biased=True, name='conv5_1')
                .batch_normalization(relu=False, name='conv5_bn1')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv5_dr1')
                .relu(name='conv5_rl1')
                .residual_block(use_dropout=True, name='conv5_residual1')
                .residual_block(use_dropout=True, name='conv5_residual2')
                .residual_block(use_dropout=True, name='conv5_residual3')
                .batch_normalization(relu=False, name='conv5_bn2')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv5_dr2')
                .relu(name='conv5_rl2')
                .conv(3, 3, 512, 1, 1, padding='SAME', relu=False, biased=True, name='conv5_2')
                .batch_normalization(relu=False, name='conv5_bn3')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv5_dr3')
                .relu(name='conv5_rl3')
                .upsampling(name='conv5_up'))

        (self.feed('conv5_up', 'conv4_rl2')
                .concat(axis=-1, name='conv6_i')
                .batch_normalization(relu=False, name='conv6_bn0')
                .conv(3, 3, 512, 1, 1, padding='SAME', relu=False, biased=True, name='conv6_1')
                .batch_normalization(relu=False, name='conv6_bn1')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv6_dr1')
                .relu(name='conv6_rl1')
                .residual_block(use_dropout=True, name='conv6_residual1')
                .residual_block(use_dropout=True, name='conv6_residual2')
                .residual_block(use_dropout=True, name='conv6_residual3')
                .residual_block(use_dropout=True, name='conv6_residual4')
                .residual_block(use_dropout=True, name='conv6_residual5')
                .residual_block(use_dropout=True, name='conv6_residual6')
                .batch_normalization(relu=False, name='conv6_bn2')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv6_dr2')
                .relu(name='conv6_rl2')
                .conv(3, 3, 256, 1, 1, padding='SAME', relu=False, biased=True, name='conv6_2')
                .batch_normalization(relu=False, name='conv6_bn3')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv6_dr3')
                .relu(name='conv6_rl3')
                .upsampling(name='conv6_up'))

        (self.feed('conv6_up', 'conv3_add_residual3')
                .concat(axis=-1, name='conv7_i')
                .batch_normalization(relu=False, name='conv7_bn0')
                .conv(3, 3, 256, 1, 1, padding='SAME', relu=False, biased=True, name='conv7_1')
                .batch_normalization(relu=False, name='conv7_bn1')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv7_dr1')
                .relu(name='conv7_rl1')
                .residual_block(use_dropout=True, name='conv7_residual1')
                .residual_block(use_dropout=True, name='conv7_residual2')
                .residual_block(use_dropout=True, name='conv7_residual3')
                .batch_normalization(relu=False, name='conv7_bn2')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv7_dr2')
                .relu(name='conv7_rl2')
                .conv(3, 3, 128, 1, 1, padding='SAME', relu=False, biased=True, name='conv7_2')
                .batch_normalization(relu=False, name='conv7_bn3')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv7_dr3')
                .relu(name='conv7_rl3')
                .upsampling(name='conv7_up'))

        (self.feed('conv7_up', 'conv2_add_residual6')
                .concat(axis=-1, name='conv8_i')
                .batch_normalization(relu=False, name='conv8_bn0')
                .conv(3, 3, 128, 1, 1, padding='SAME', relu=False, biased=True, name='conv8_1')
                .batch_normalization(relu=False, name='conv8_bn1')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv8_dr1')
                .relu(name='conv8_rl1')
                .residual_block(use_dropout=True, name='conv8_residual1')
                .residual_block(use_dropout=True, name='conv8_residual2')
                .residual_block(use_dropout=True, name='conv8_residual3')
                .batch_normalization(relu=False, name='conv8_bn2')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv8_dr2')
                .relu(name='conv8_rl2')
                .conv(3, 3, 64, 1, 1, padding='SAME', relu=False, biased=True, name='conv8_2')
                .batch_normalization(relu=False, name='conv8_bn3')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv8_dr3')
                .relu(name='conv8_rl3')
                .upsampling(name='conv8_up'))

        (self.feed('conv8_up', 'conv1_add_residual8')
                .concat(axis=-1, name='conv9_i')
                .batch_normalization(relu=False, name='conv9_bn0')
                .conv(3, 3, 64, 1, 1, padding='SAME', relu=False, biased=True, name='conv9_1')
                .batch_normalization(relu=False, name='conv9_bn1')
                .dropout(keep_prob=0.8, is_training=is_training, name='conv9_dr1')
                .relu(name='conv9_rl1')
                .conv(3, 3, 3, 1, 1, padding='SAME', relu=False, biased=False, name='conv9_2'))
