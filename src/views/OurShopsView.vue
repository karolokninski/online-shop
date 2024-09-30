<template>
  <div class="min-h-screen flex flex-col bg-white">
    <TopBar></TopBar>
    <div class="flex-grow container mx-auto py-10 mt-20" style="justify-content: center; align-items: center ; text-align: center;">
      <h2 class="text-2xl font-bold mb-4" style="margin-top: 2rem;">Nasze Sklepy</h2>
        <div class="flex flex-col md:flex-row space-y-6 md:space-y-0 md:space-x-6">
          <div class="container mx-auto py-9">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
              <div class="rounded-md overflow-hidden">
                <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2436.839393374339!2d21.012228415810946!3d52.2296752797588!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x471ecc669cecb647%3A0x2b0f9aafb206b44f!2sWarszawa!5e0!3m2!1spl!2spl!4v1635352330339!5m2!1spl!2spl"
                  width="100%" 
                  height="300" 
                  style="border:0;" 
                  allowfullscreen="" 
                  loading="lazy">
                </iframe>
              </div>
              <div class="rounded-md overflow-hidden">
                <iframe 
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2436.839393374339!2d21.012228415810946!3d52.2296752797588!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x471ecc669cecb647%3A0x2b0f9aafb206b44f!2sWarszawa!5e0!3m2!1spl!2spl!4v1635352330339!5m2!1spl!2spl"
                  width="100%" 
                  height="300" 
                  style="border:0;" 
                  allowfullscreen="" 
                  loading="lazy">
                </iframe>
              </div>
              <div class="rounded-md overflow-hidden">
                <iframe 
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2449.5677896236636!2d19.93505931579872!3d50.05664997942366!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47165b0d3b7aa641%3A0xa861b4719fdc2f40!2sKrak%C3%B3w!5e0!3m2!1spl!2spl!4v1635352330339!5m2!1spl!2spl"
                  width="100%" 
                  height="300" 
                  style="border:0;" 
                  allowfullscreen="" 
                  loading="lazy">
                </iframe>
              </div>
            <div class="rounded-md overflow-hidden">
              <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2429.959866738667!2d18.606675415818577!3d54.352025179355654!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46fd74c6d960dd7d%3A0x6f29b2fa0f20c4a0!2sGda%C5%84sk!5e0!3m2!1spl!2spl!4v1635352330339!5m2!1spl!2spl"
                width="100%" 
                height="300" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy">
              </iframe>
            </div>
          </div>
        </div>
      </div>
    </div>     
    <Footer></Footer>
  </div>
</template>
    
<script setup>
  import TopBar from '@/components/TopBar.vue';
  import Footer from '@/components/Footer.vue';
</script>