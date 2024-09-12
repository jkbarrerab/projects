
import tensorflow as tf
from tensorflow.keras.layers import Dense, Reshape, Flatten, Conv2D, Conv2DTranspose, LeakyReLU, Dropout
from tensorflow.keras.models import Sequential

# Define the generator
def build_generator(latent_dim):
    model = Sequential()
    model.add(Dense(256 * 16 * 16, activation="relu", input_dim=latent_dim))
    model.add(Reshape((16, 16, 256)))
    model.add(Conv2DTranspose(128, kernel_size=4, strides=2, padding='same'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(Conv2DTranspose(64, kernel_size=4, strides=2, padding='same'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(Conv2D(1, kernel_size=5, activation='tanh', padding='same'))
    return model

# Define the discriminator
def build_discriminator(img_shape):
    model = Sequential()
    model.add(Conv2D(64, kernel_size=4, strides=2, input_shape=img_shape, padding='same'))
    model.add(LeakyReLU(alpha=0.25))
    model.add(Dropout(0.3))
    model.add(Conv2D(128, kernel_size=4, strides=2, padding='same'))
    model.add(LeakyReLU(alpha=0.25))
    model.add(Dropout(0.3))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    return model

# Compile the GAN
def compile_gan(generator, discriminator):
    discriminator.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    discriminator.trainable = False
    gan_input = tf.keras.Input(shape=(latent_dim,))
    generated_image = generator(gan_input)
    gan_output = discriminator(generated_image)
    gan = tf.keras.Model(gan_input, gan_output)
    gan.compile(optimizer='adam', loss='binary_crossentropy')
    return gan

# Hyperparameters
latent_dim = 100
img_shape = (128, 128, 1)

# Create the models
generator = build_generator(latent_dim)
discriminator = build_discriminator(img_shape)
gan = compile_gan(generator, discriminator)

# Training loop (simplified)
def train_gan(epochs, batch_size):
    for epoch in range(epochs):
        # Train discriminator
        noise = tf.random.normal([batch_size, latent_dim])
        generated_images = generator.predict(noise)
        real_images = ... # Load real images here
        labels_real = tf.ones((batch_size, 1))
        labels_fake = tf.zeros((batch_size, 1))
        d_loss_real = discriminator.train_on_batch(real_images, labels_real)
        d_loss_fake = discriminator.train_on_batch(generated_images, labels_fake)
        
        # Train generator
        noise = tf.random.normal([batch_size, latent_dim])
        labels_gan = tf.ones((batch_size, 1))
        g_loss = gan.train_on_batch(noise, labels_gan)
        
        # Log the progress
        print(f'Epoch {epoch}, D Loss: {d_loss_real + d_loss_fake}, G Loss: {g_loss}')

train_gan(epochs=10000, batch_size=64)


