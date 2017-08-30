import tensorflow as tf

tf.app.flags.DEFINE_string('fold_dir', '', 'Folder directory')

tf.app.flags.DEFINE_string('data_dir', '', 'Data directory')

tf.app.flags.DEFINE_string('output_dir', '', 'Output directory')

tf.app.flags.DEFINE_string('train_list', 'age_train.txt',
                           'Training list')

tf.app.flags.DEFINE_string('valid_list', 'age_val.txt',
                           'Test list')

tf.app.flags.DEFINE_integer('train_shards', 10,
                            'Number of shards in training TFRecord files.')

tf.app.flags.DEFINE_integer('valid_shards', 2,
                            'Number of shards in validation TFRecord files.')

tf.app.flags.DEFINE_integer('num_threads', 2,
                            'Number of threads to preprocess the images.')

FLAGS = tf.app.flags

