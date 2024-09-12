# Projeto AdminBN :desktop_computer:

<div align="center">
<img src="https://github.com/user-attachments/assets/26a3c26c-6987-450f-8912-0ed36f82be1c" width="700px" />
</div>

### Objetivo:

Este repostório foi criado para o projeto de conclusão da disciplina de Projeto Integrador.
Os arquivos aqui contidos servem para executar o projeto, aqui constam arquivos de
configuração, execução do projeto e arquivos de orientação, bem como as sprints do projeto.

### Proposta de Projeto Integrador
#### Título da proposta

AdminBN - Administração de Ativos e Serviços de Redes com Telegram em Redes de Pequeno Porte

#### Resumo da proposta
Este projeto propõe uma solução para a administração de serviços de redes em ambientes de pequeno porte, utilizando a plataforma de mensagens Telegram como interface de controle. A implementação de comandos em um bot do Telegram permitirá configurar e monitorar serviços de rede, como servidores DHCP, firewall, entre outros, de forma remota. A utilização do Telegram como interface de controle oferece uma experiência de usuário simplificada e intuitiva. Muitos usuários já estão familiarizados com a plataforma de mensagens, o que reduz o tempo de aprendizado com a ferramenta e torna a administração de redes mais acessível para diversos perfis. Além disso, o Telegram é uma aplicação multiplataforma, disponível em dispositivos móveis e desktops, o que significa que os administradores podem gerenciar os seus ativos e serviços de redes em qualquer lugar, a qualquer momento. Em ambientes de pequeno porte, onde muitas das vezes os recursos podem ser limitados, uma solução baseada em Telegram pode ser mais acessível do que investir em softwares ou equipamentos dedicados para administração de redes. Isso representa uma economia significativa de recursos e gastos para a empresa. Um outro ponto que vale elencar é que a capacidade de configurar e monitorar serviços de rede remotamente, através de comandos simples no Telegram, aumenta a agilidade e eficiência dos processos, garantindo assim uma resposta mais rápida a eventuais problemas ou necessidades de configuração, garantindo uma operação mais fluida e eficaz das redes.

O projeto é destinado para administradores de redes, técnicos e empresas de pequeno porte que buscam uma solução inovadora ou acessível para a administração de seus serviços e ativos de redes. A facilidade de acesso e a economia de recursos tornam essa solução especialmente relevante para ambientes com limitações de orçamento e infraestrutura, proporcionando uma maneira econômica e eficaz de gerenciar redes.

A entrega do MVP (Minimum Viable Product) deste projeto consistirá na implementação básica do bot Telegram, capaz de interpretar comandos específicos para a administração de serviços de redes em ambientes de pequeno porte. Nesta fase inicial, o foco estará na funcionalidade essencial do sistema, permitindo aos usuários realizar operações básicas de configuração e monitoramento de serviços como servidores DHCP e firewall. O MVP oferecerá uma interface simples e intuitiva, possibilitando que os administradores de redes e técnicos testam a solução e forneçam feedback sobre sua usabilidade e eficácia. Embora possa não incluir todos os recursos planejados a longo prazo, o MVP será funcional o suficiente para demonstrar o conceito e validar a viabilidade técnica e comercial do projeto. A entrega do MVP será acompanhada por testes a fim de garantir sua estabilidade e confiabilidade.

O projeto incorpora uma variedade de disciplinas essenciais para seu desenvolvimento e implementação. A matéria de Administração de Sistemas Abertos desempenha um papel fundamental na configuração dos serviços de rede cruciais, como servidores DHCP e DNS. Esta disciplina permite garantir o funcionamento e a disponibilidade dos recursos necessários para facilitar a comunicação na rede. A matéria de Programação para Redes é de suma importância, pois é empregada na implementação de sockets para a comunicação cliente/servidor com o bot do Telegram. Essa habilidade é vital para estabelecer uma interação eficaz entre o bot, os servidores e os administradores, possibilitando o envio e recebimento de comandos. Além disso, a matéria de Administração avançada de serviços de redes é uma disciplina crítica neste projeto para abordar aspectos avançados de administração de redes, como gerenciamento de tráfego, otimização de desempenho e resolução de problemas complexos de rede. Cada uma dessas disciplinas desempenha um papel indispensável na construção do MVP, assegurando que o sistema atenda aos requisitos funcionais.

#### Introdução
A administração eficaz de serviços e ativos de redes em ambientes de pequeno porte representa um desafio significativo para muitas organizações. A complexidade crescente das infraestruturas de rede, junto ao fato da escassez de recursos técnicos e financeiros, pode resultar em dificuldades na configuração, manutenção e monitoramento dos serviços e ativos essenciais. Como ressalta Al-Fuqaha et al. (2015), "a gestão eficiente de redes é vital para garantir a operação contínua e a segurança das infraestruturas de rede". Além disso, conforme destacado por Douligeris e Serpanos (2011), "a segurança da rede é uma preocupação crítica em todos os níveis de implementação e gerenciamento de redes". No entanto, muitas vezes, os recursos limitados por parte da empresa impedem a implementação de soluções robustas.

Diante desse cenário, surge a necessidade de uma solução inovadora e acessível que simplifique essa demanda. Neste contexto, propomos a utilização da plataforma de mensagens Telegram como uma ferramenta de controle para configurar e monitorar serviços e ativos das redes de pequeno porte. Ao desenvolver um bot Telegram capaz de interpretar comandos específicos para administração dos mesmos, oferecemos uma solução prática e econômica para superar os desafios enfrentados pelos administradores e técnicos. Essa abordagem não só simplifica a administração de redes, mas também contribui para a democratização do acesso a ferramentas de tecnologia da informação e comunicação, alinhando-se com as demandas por eficiência e acessibilidade em contextos empresariais e organizacionais.

O diferencial deste projeto reside em sua abordagem inovadora e acessível. Ao utilizar o Telegram como interface de controle para configurar e monitorar serviços de rede, a solução se destaca pela simplicidade de uso, aproveitando a familiaridade e acessibilidade da plataforma de mensagens. Essa abordagem elimina a necessidade de treinamento extensivo, tornando a atividade mais fácil e intuitiva para uma variedade de usuários. Além disso, a acessibilidade do Telegram em dispositivos móveis e desktops proporciona maior flexibilidade, permitindo gerenciar os serviços e ativos de qualquer lugar e a qualquer momento. Em ambientes com recursos limitados, a solução baseada em Telegram oferece uma alternativa econômica em comparação com softwares ou equipamentos dedicados, representando uma economia significativa de recursos. Mais a frente iremos detalhar os objetivos específicos, sprints e tarefas associadas.

#### Justificativa
A relevância deste projeto é evidenciada pela crescente necessidade de simplificar e democratizar a configuração, manutenção e monitoramento dos ativos e serviços de rede, onde os recursos técnicos e financeiros muitas vezes são limitados. A abordagem inovadora de utilizar o Telegram como interface de controle para configurar e monitorar serviços de rede oferece uma solução prática e acessível para superar os desafios enfrentados por administradores, técnicos e empresas nesses contextos. Além disso, a agilidade e eficiência proporcionadas por essa solução contribuem para melhorar a operação, promovendo um ambiente de trabalho mais produtivo e confiável.

Integração das Disciplinas:
Administração de Sistemas Abertos: Esta disciplina será integrada ao projeto para configurar os serviços de rede, como servidores DHCP e DNS, conforme mencionado na justificativa do projeto. A ementa desta disciplina geralmente abrange tópicos como configuração e administração de serviços de rede em sistemas operacionais de código aberto, o que é essencial para garantir o funcionamento adequado dos serviços de rede no ambiente proposto pelo projeto.

Programação para Redes: A Programação para Redes será integrada ao projeto para implementar a comunicação cliente/servidor com o bot do Telegram, utilizando sockets. A ementa dessa disciplina geralmente inclui tópicos como comunicação de dados em redes, protocolos de rede e implementação de aplicações de rede, fornecendo os conhecimentos necessários para desenvolver a interação entre o bot Telegram e os administradores de rede.

Administração Avançada de Redes: Esta disciplina será integrada ao projeto para abordar aspectos avançados de administração de redes, como gerenciamento de tráfego, otimização de desempenho e resolução de problemas complexos de rede. A ementa dessa disciplina geralmente cobre tópicos relacionados à administração avançada de serviços de rede e infraestrutura de rede, o que é essencial para garantir a eficiência e segurança das redes no contexto do projeto.

A integração dessas disciplinas ao projeto permitirá abordar os aspectos técnicos fundamentais necessários para o desenvolvimento e implementação bem-sucedidos da solução proposta, garantindo que ela atenda às necessidades.

#### Objetivo Geral e Objetivos Específicos
Objetivo Geral:
O objetivo geral deste projeto é desenvolver e implementar uma solução inovadora e acessível para a administração de serviços e ativos de rede, utilizando a plataforma de mensagens Telegram como interface de controle.


Objetivos Específicos:
Desenvolver um bot Telegram capaz de interpretar comandos específicos para administração de serviços de redes, como configuração de servidores DHCP, DNS, firewall, entre outros.

Integrar o bot Telegram com os serviços de redes mais comuns, garantindo a comunicação eficaz e a execução de comandos de forma segura e confiável.

Testar a funcionalidade e usabilidade da solução em ambientes simulados e reais de redes de pequeno porte, coletando feedback dos usuários para ajustes e melhorias.

Avaliar o desempenho e eficácia da solução, considerando critérios como facilidade de uso, economia de recursos e benefícios para os administradores de redes.

Contribuir para a disseminação de soluções inovadoras e acessíveis na área de administração de redes, promovendo uma maior democratização do acesso a ferramentas de tecnologia da informação e comunicação.

#### Entregas
Sprint 1: Planejamento e Preparação

Definir os requisitos detalhados do sistema, incluindo os comandos do bot Telegram e os serviços de redes a serem integrados.
Estabelecer a arquitetura geral do sistema e definir as tecnologias a serem utilizadas.
Criar um plano detalhado de projeto, incluindo cronograma, alocação de recursos e metas específicas para cada sprint subsequente.


Sprint 2: Desenvolvimento do Bot Telegram

Desenvolver e testar as funcionalidades básicas do bot Telegram, incluindo a capacidade de receber e interpretar comandos dos usuários.
Implementar a lógica de negócios inicial para responder aos comandos relacionados à administração de redes.


Sprint 3: Integração com Serviços de Redes

Integrar o bot Telegram com os serviços de redes mais comuns, como servidores DHCP, DNS, firewall e Hotspot.
Estabelecer a comunicação eficaz entre o bot e os serviços de redes, garantindo a execução dos comandos.


Sprint 4: Implementação de Recursos Avançados

Desenvolver recursos avançados para o bot Telegram, como autenticação básica
Realizar testes extensivos para garantir a estabilidade e funcionalidade dos novos recursos implementados.


Sprint 5: Testes e Ajustes

Realizar correções de Bugs e implementar possíveis novas funções que venham a surgir, de acordo com os problemas enfrentados no Sprint Anterior


Sprint 6: Avaliação e Entrega Final

Avaliar o desempenho e eficácia da solução, considerando critérios como facilidade de uso, economia de recursos e benefícios para os administradores de redes.
Preparar a documentação final do projeto e realizar a entrega da solução.


#### Disciplinas Escolhidas
1. Arquitetura TCP/IP
2. Programação para Redes
3. Administração de Sistemas Abertos
4. Administração Avançada de Serviços de Redes
5. Introdução aos Sistemas Abertos
