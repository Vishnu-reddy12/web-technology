{ name: 'Tata Elect', logo: 'https://ekhie.org/wp-content/uploads/2024/03/tata-elect.jpg', industry: 'Manufacturing/Engineering' },
  { name: 'Frontline', logo: 'https://ekhie.org/wp-content/uploads/2024/03/frontline.jpg', industry: 'Business Services' },
  { name: 'Yamaha', logo: 'https://ekhie.org/wp-content/uploads/2024/03/yamaha.png', industry: 'Automotive/Manufacturing' },
  { name: 'Pronion', logo: 'https://ekhie.org/wp-content/uploads/2024/03/pronion.jpg', industry: 'Technology' },
  { name: 'Technopark', logo: 'https://ekhie.org/wp-content/uploads/2024/03/technopark.png', industry: 'IT/Technology Park' },
  { name: 'IRT', logo: 'https://ekhie.org/wp-content/uploads/2024/03/irt.png', industry: 'Research/Technology' },
  { name: 'Alphacraft', logo: 'https://ekhie.org/wp-content/uploads/2024/03/alphacraft.jpg', industry: 'Manufacturing' },
  { name: 'Gabriel', logo: 'https://ekhie.org/wp-content/uploads/2024/03/gabriel.png', industry: 'Automotive Parts' },
  { name: 'Infinity', logo: 'https://ekhie.org/wp-content/uploads/2024/03/infinity.jpg', industry: 'Technology/Services' },
  { name: 'Neyes', logo: 'https://ekhie.org/wp-content/uploads/2024/03/neyes.png', industry: 'Technology/Services' },
  { name: 'Quantum', logo: 'https://ekhie.org/wp-content/uploads/2024/03/quantum.jpeg', industry: 'Technology/Services' },
  { name: 'VLT', logo: 'https://ekhie.org/wp-content/uploads/2024/10/logo-vlt.png', industry: 'Technology/Services' },
  { name: 'Vintorix', logo: '/lovable-uploads/e8397839-5667-4624-81d5-aa4b93d977b4.png', industry: 'Technology/Services' },
  { name: 'SimpleSolve', logo: '/lovable-uploads/c5bbb63f-ad23-491e-8407-8a14124cd451.png', industry: 'Technology/Services' },
  { name: 'PDS Perfect Detailing Services', logo: '/lovable-uploads/7e11ae14-cef4-49d9-930d-1497de474c4e.png', industry: 'Detailing Services' },
  { name: 'Vulture Lines', logo: '/lovable-uploads/87e48afc-ad90-4af5-bb0a-fe17fa8ef259.png', industry: 'Technology/Services' },
  { name: 'Technical Trader 515', logo: '/lovable-uploads/f31f0ebc-ea9a-453c-a011-ca7fbcb9e4d1.png', industry: 'Financial/Trading' }
];

const recentClients = [
  { name: 'Recent Client 1', logo: 'https://ekhie.org/wp-content/uploads/2024/10/WhatsApp-Image-2024-10-09-at-7.05.53-PM.jpeg', date: 'Oct 2024' },
  { name: 'VLT', logo: 'https://ekhie.org/wp-content/uploads/2024/10/logo-vlt.png', date: 'Oct 2024' },
  { name: 'Recent Client 2', logo: 'https://ekhie.org/wp-content/uploads/2025/03/WhatsApp-Image-2025-03-11-at-9.58.33-AM.jpeg', date: 'Mar 2025' },
  { name: 'Recent Client 3', logo: 'https://ekhie.org/wp-content/uploads/2025/03/WhatsApp-Image-2025-03-11-at-9.57.27-AM-1.jpeg', date: 'Mar 2025' },
  { name: 'Recent Client 4', logo: 'https://ekhie.org/wp-content/uploads/2025/03/WhatsApp-Image-2025-03-11-at-9.57.27-AM.jpeg', date: 'Mar 2025' },
  { name: 'Recent Client 5', logo: 'https://ekhie.org/wp-content/uploads/2025/03/WhatsApp-Image-2025-03-11-at-9.57.26-AM.jpeg', date: 'Mar 2025' },
  { name: 'Vintorix', logo: '/lovable-uploads/e8397839-5667-4624-81d5-aa4b93d977b4.png', date: 'Recent' },
  { name: 'SimpleSolve', logo: '/lovable-uploads/c5bbb63f-ad23-491e-8407-8a14124cd451.png', date: 'Recent' }
];

const ClientsSlider = () => {
  return (
    <section className="py-16 bg-white border-t border-gray-100 relative z-10">
      <div className="container-custom">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">Trusted by Leading Companies</h2>
          <p className="text-gray-600 max-w-2xl mx-auto">
            We're proud to work with industry leaders and innovative companies across various sectors
          </p>
        </div>
        
        {/* Main clients marquee */}
        <div className="relative overflow-hidden mb-16 bg-gray-50 py-8 rounded-lg">
          <style jsx>{`
            @keyframes marquee {
              0% { transform: translateX(0%); }
              100% { transform: translateX(-50%); }
            }
            .animate-marquee {
              animation: marquee 30s linear infinite;
            }
            .animate-marquee:hover {
              animation-play-state: paused;
            }
          `}</style>
          
          <div className="flex space-x-16 animate-marquee">
            {/* First set of clients */}
            {clients.map((client, index) => (
              <div key={`${client.name}-${index}`} className="flex items-center justify-center min-w-[200px] h-20 flex-shrink-0">
                <img 
                  src={client.logo} 
                  alt={`${client.name} logo`} 
                  className="max-h-16 max-w-[180px] grayscale hover:grayscale-0 transition-all duration-300 object-contain filter brightness-75 hover:brightness-100"
                  onError={(e) => {
                    const target = e.target as HTMLImageElement;
                    target.src = 'https://via.placeholder.com/180x60/f3f4f6/6b7280?text=' + encodeURIComponent(client.name);
                  }}
                />
              </div>
            ))}
            {/* Duplicate set for infinite loop */}
            {clients.map((client, index) => (
              <div key={`${client.name}-duplicate-${index}`} className="flex items-center justify-center min-w-[200px] h-20 flex-shrink-0">
                <img 
                  src={client.logo} 
                  alt={`${client.name} logo`} 
                  className="max-h-16 max-w-[180px] grayscale hover:grayscale-0 transition-all duration-300 object-contain filter brightness-75 hover:brightness-100"
                  onError={(e) => {
                    const target = e.target as HTMLImageElement;
                    target.src = 'https://via.placeholder.com/180x60/f3f4f6/6b7280?text=' + encodeURIComponent(client.name);
                  }}
                />
              </div>
            ))}
          </div>
        </div>
        
        {/* Recent Partners Section */}
        <div>
          <h3 className="text-2xl font-semibold text-center mb-8 text-gray-900">Recent Partners</h3>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6">
            {recentClients.map((client, index) => (
              <div key={`recent-${index}`} className="flex flex-col items-center bg-white p-6 rounded-lg shadow-sm border border-gray-200 hover:shadow-md transition-shadow">
                <div className="h-20 flex items-center justify-center mb-3 w-full">
                  <img 
                    src={client.logo}
                    alt={`${client.name} logo`}
                    className="max-h-16 max-w-full object-contain"
                    onError={(e) => {
                      const target = e.target as HTMLImageElement;
                      target.src = 'https://via.placeholder.com/150x60/f3f4f6/6b7280?text=' + encodeURIComponent(client.name);
                    }}
                  />
                </div>
                <span className="text-sm text-gray-500 font-medium">{client.date}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default ClientsSlider;

