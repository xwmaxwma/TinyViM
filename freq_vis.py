# Call the following functions wherever visualisation is required

def visualize_freq(x, fig_name='low.png'):
    '''
    x : The output feature maps from either High or Low branch.
    Tensor shape: (b,c,h,w)
    '''
    print(x.shape)
    import matplotlib.pyplot as plt

    fft_output = torch.fft.fft2(x.float())
    freq_img = torch.log(torch.abs(torch.fft.fftshift(fft_output)))
    num_plots = 4
    # average over samples
    freq_img_mean = freq_img.mean(dim=0).cpu()
    fig, axis = plt.subplots(1, num_plots, figsize=(num_plots * 4, 4))
    for i in range(num_plots):
        axis[i].imshow(freq_img_mean[i+4, ...].numpy())
        axis[i].axes.xaxis.set_visible(False)
        axis[i].axes.yaxis.set_visible(False)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('fig/'+fig_name)
    plt.close()

def visualize_amp(xs, fig_name='amp.png'):
    '''
    x : The output feature maps from either High or Low branch.
    Tensor shape: (b,c,h,w)
    '''
    import matplotlib.pyplot as plt

    # fft_output = torch.fft.fft2(x.float())
    # freq_img = torch.log(torch.abs(torch.fft.fftshift(fft_output)))
    latent_list = []

    for x in xs:
        freq_img = (torch.fft.fft2(x.float()).abs()).log()
        b, c, h, w = freq_img.shape
        freq_img = torch.roll(freq_img, shifts=(int(h/2), int(w/2)), dims=(2, 3))
        # average over samples
        freq_img_mean = freq_img.mean(dim=(0,1)).cpu()

        latent = freq_img_mean.diag()[int(h/2):] 
        # print(latent)
        latent = latent - latent[0]
        latent_list.append(latent)
    
    fig, ax1 = plt.subplots(1, 1, figsize=(5, 4), dpi=150)
    labels = ['before', 'after']
    colors = ['blue', 'red']
    import numpy as np
    import matplotlib.cm as cm
    for i in range(len(latent_list)):
        latent = latent_list[i]
        freq = np.linspace(0, 1, len(latent))
        ax1.plot(freq, latent, color=colors[i],label=labels[i])
    plt.legend(fontsize='16')
    ax1.set_xlim(left=0, right=1)
    ax1.set_xlabel("Frequency")
    ax1.set_ylabel("$\Delta$ Log amplitude")
    from matplotlib.ticker import FormatStrFormatter
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1fπ'))
    # print(freq_img_mean.shape)
    # print(freq_img_mean)
    # plt.axis('off')
    plt.tight_layout()
    plt.savefig('fig/'+fig_name)
    plt.close()
